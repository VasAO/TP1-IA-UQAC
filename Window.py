from tkinter import *

class Window:
   """
   La classe Window permet d'afficher le résultat de l'environement à un instant t
   L'affichage est géré avec Tkinter, une librairie permettant de créer et manipuler des fenêtres en Python
   """
   def __init__(self, width, height, resizable, title, board):
      self.width = width
      self.height = height
      self.resizable = resizable
      self.title = title or "TP1 IA"
      self.instance = None
      self.board = board

   def create_window(self):
      self.instance = Tk()
      self.instance.geometry(f"{self.width}x{self.height}")
      self.instance.resizable(width = self.resizable, height = self.resizable)
      self.instance.title(self.title)

   def mainloop(self):
      self.instance.mainloop()