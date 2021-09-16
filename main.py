from Board import Board
from Window import Window
from Robot import Robot
import time

b = Board()
r = Robot(b)
w = Window(500, 500, False, "TP1 IA", b, r)
w.display_board()

while(True): 
   # b.random_dust_jewel()
   # r.move_left()
   # w.display_board()
   time.sleep(1)


w.mainloop()