
from Board import Board
from Window import Window

board = Board()
w = Window(500, 500, False, "TP1 IA", board)
w.create_window()

w.mainloop()

# C = Canvas(w, bg="blue", height=250, width=300)

# coord = 10, 50, 240, 210
# arc = C.create_arc(coord, start=0, extent=150, fill="red")

# C.pack()
