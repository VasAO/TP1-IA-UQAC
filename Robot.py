import random

class Robot:
   def __init__(self, counter=20):
      self.x = random.randint(0, 4)
      self.y = random.randint(0, 4)
      self.counter = counter

   def get_x(self):
      return self.x

   def get_y(self):
      return self.y