The-Mystery-Box-Solver
======================
@author Jason Giancono

A program to give the optimal move for a state in the Warcraft 3 Mod Uther Party 2's minigame "The Mystery Box"

Also gives the option to output a graph of the minmax tree it generates, but this requires the python ETE2 which only really works out-of-the-box.

USAGE: uther.py <flag> [players] [time]

                flags:
                -cmd:   Use text prompt interface
                -gui:   Use GUI interface
                -ni:    Use no interface, must follow by number
                        of players and number of turns
