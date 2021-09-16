from Board import Board
from Window import Window
from Robot import Robot
import time

b = Board()
r = Robot(b)
w = Window(500, 500, False, "TP1 IA", b, r)
w.display_board()

counter = 0

while(True): 
   if(counter % 3 == 0): b.random_dust_jewel()

   goal = r.select_nearest_not_empty_room()
   r.reach_selected_room(goal)
   
   counter += 1
   w.display_board()
   time.sleep(1)

# Todo: Gérer le cas ou toutes les pièces sont vides
w.mainloop()