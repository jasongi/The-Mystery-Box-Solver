import string
from Tkinter import *
class uther(Frame):
	def __init__(self,Master=None,*pos,**kw):
		#
		#Your code here
		#
		self.label = StringVar()
		apply(Frame.__init__,(self,Master),kw)
		self._Frame3 = Frame(self)
		self._Frame3.pack(side='top')
		self._Label3 = Label(self._Frame3,text='Players Left')
		self._Label3.pack(anchor='e',side='left')
		self._Entry2 = Entry(self._Frame3)
		self._Entry2.pack(anchor='w',side='left')
		self._Entry2.bind('<Return>',self._on_Button1_ButRel_1)
		self._Frame2 = Frame(self)
		self._Frame2.pack(side='top')
		self._Label2 = Label(self._Frame2,text='Box Number')
		self._Label2.pack(anchor='e',side='left')
		self._Entry1 = Entry(self._Frame2)
		self._Entry1.pack(anchor='w',side='left')
		self._Entry1.bind('<Return>',self._on_Button1_ButRel_1)

		self._Frame4 = Frame(self)
		self._Frame4.pack(side='top')
		self._Button1 = Button(self._Frame4,text='Generate')
		self._Button1.pack(anchor='w',side='left')
		self._Button1.bind('<ButtonRelease-1>',self._on_Button1_ButRel_1)
		self._Frame5 = Frame(self)
		self._Frame5.pack(side='top')
		self._Button2 = Button(self._Frame5,text='Save (must be on Linux with ETE2)')
		self._Button2.pack(anchor='e',side='left')
		self._Button2.bind('<ButtonRelease-1>',self._on_Button2_ButRel_1)
		self._Frame1 = Frame(self)
		self._Frame1.pack(side='top')
		self._Label1 = Label(self._Frame1,textvariable=self.label)
		self._Label1.pack(anchor='e',side='top')
		self.label.set('Your Move: None')
	def _on_Button1_ButRel_1(self,Event=None):
		players = int(float(self._Entry2.get()))
		timer = int(float(self._Entry1.get()))
		tree = MinMax(players, timer)
		if (tree.doMove > 0):
			self.label.set('Your Move: ' + str(tree.doMove) + '\nCosts for Players: ' + str(tree.head.costs))
		else:
			self.label.set("It doesn't matter, you dead")

	def _on_Button2_ButRel_1(self,Event=None):
		from ete2 import Tree
		from ete2 import TreeStyle
		players = int(float(self._Entry2.get()))
		timer = int(float(self._Entry1.get()))
		tree = MinMax(players, timer)
		ts = TreeStyle()
		ts.rotation=270
		ts.show_leaf_name=True
		t = Tree(newick='('+tree.head.getKids('Start')+');', format=0)
		t.render(file_name="uther.svg",tree_style=ts)
class MinMax:
	def __init__(self,players, timer):
		self.numPlayers = players-1
		self.head = MinNode(timer, 0, players)
		self.doMove = self.head.max()

class MinNode:
	def __init__(self,timer, turn, players):
		self.costs = []
		self.bestPath = None
		self.timer = timer
		self.turn = turn
		self.players = players
		if (self.timer > 0):
			self.left = MinNode(self.timer-1,turn+1,players)
			self.right = MinNode(self.timer-2, turn+1,players)
			if (self.timer-2 < 0):
				self.right.costs = []
				for ii in range(self.players):
					if (self.turn%self.players == ii):
						self.right.costs.append(0)
					else: 
						self.right.costs.append(1)
		else:
			self.left = None
			self.right = None
			for ii in range(self.players):
				if (self.turn%self.players == ii):
					self.costs.append(0)
				else: 
					self.costs.append(1)
	def max(self):
		if(self.costs == []):
			self.right.max()
			self.left.max()
			self.bestPath = 0
			if (self.right.costs[self.turn%self.players] > self.left.costs[self.turn%self.players]):
				self.costs = self.right.costs
				self.bestPath = 2
			elif (self.right.costs[self.turn%self.players] < self.left.costs[self.turn%self.players]):
				self.costs = self.left.costs
				self.bestPath = 1
			else:
				for ii in range(self.players):
					self.costs.append(float(self.right.costs[ii]+self.left.costs[ii])/2.0)
					self.bestPath = '2 or 1'
		return self.bestPath
	def getKids(self, label):
		if (self.right is None):
			return label + '' + string.replace(string.replace(string.replace(string.replace(str(self.costs),',',''),' ', ''),'[',''),']','')
		else:
			return '('+self.left.getKids('Q')+','+self.right.getKids('W')+')'+ label + '' + string.replace(string.replace(string.replace(string.replace(str(self.costs),',',''),' ', ''),'[',''),']','')

if ((len(sys.argv) == 2 and sys.argv[1] == '-cmd')):
	players = input("Input number of players: ")
	timer = input("Input timer number: ")
	tree = MinMax(players, timer)
	if (tree.doMove > 0):
		print tree.doMove
		print tree.head.costs
	else:
		print "It doesn't matter, you dead"
	if (raw_input('Render? Only if on Windows and have ETE2 package y/n: ') == 'y'):
		from ete2 import Tree
		from ete2 import TreeStyle
		ts = TreeStyle()
		ts.rotation=270
		ts.show_leaf_name=True
		t = Tree(newick='('+tree.head.getKids('Start')+');', format=0)
		t.render(file_name="uther.svg",tree_style=ts)
		print "Saved graph to uther.svg"
elif (len(sys.argv) == 2 and sys.argv[1] == '-gui'):
		#Adjust sys.path so we can find other modules of this project
		import sys
		if '.' not in sys.path:
			sys.path.append('.')
		#Put lines to import other modules of this project here
		
		if __name__ == '__main__':
			Root = Tk()
			import Tkinter

			del Tkinter
			App = uther(Root)
			App.pack(expand='yes',fill='both')

			Root.geometry('360x150+10+10')
			Root.title('uther')
			Root.mainloop()
elif ((len(sys.argv) == 4) and sys.argv[1] == '-ni'):
	players = int(sys.argv[2])
	timer = int(sys.argv[3])
	tree = MinMax(players, timer)
	if (tree.doMove > 0):
		print tree.doMove
		print tree.head.costs
	else:
		print "It doesn't matter, you dead"
	if (raw_input('Render? Only if on Windows and have ETE2 package y/n: ') == 'y'):
		from ete2 import Tree
		from ete2 import TreeStyle
		ts = TreeStyle()
		ts.rotation=270
		ts.show_leaf_name=True
		t = Tree(newick='('+tree.head.getKids('Start')+');', format=0)
		t.render(file_name="uther.svg",tree_style=ts)
		print "Saved graph to uther.svg"
else:
	print 'USAGE: uther.py <flag> [players] [time]\n\n\t\tflags:\n\t\t-cmd: \tUse text prompt interface\n\t\t-gui: \tUse GUI interface\n\t\t-ni: \tUse no interface, must follow by number \n\t\t\tof players and number of turns'
