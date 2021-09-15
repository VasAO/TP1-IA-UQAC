import random

class Board:
   """
   La classe Board permet de représenter l'environment. Le manoir de 5x5 pièces.
   Chaque pièce peut contenir de la poussière, des bijoux et rien.
      0 => rien
      1 => bijoux
      2 => poussière

   La répartition des éléments dans les pièces est faite de manière pseudo-aléatoire.
   """
   def __init__(self):
      self.board = [[0 for j in range(5)] for i in range(5)]
      self.init_board()

   def init_board(self):
      for i in range(5):
         for j in range(5):
            self.board[i][j] = random.randint(0, 2)