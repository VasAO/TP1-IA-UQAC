from Board import Board
from Window import Window
from Robot import Robot
import time

r = Robot()
b = Board(r)
w = Window(500, 500, False, "TP1 IA", b)
w.display_board()

while(True):
   b.random_dust_jewel()
   w.display_board()
   time.sleep(.1)

w.mainloop()