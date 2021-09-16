import random
import math

class Robot:
    """
    La classe Robot représent l'agent intelligent qui peut intéragir et parcourir son environnement.
    Il possède des coordonnées x et y afin de pouvoir le localiser.
    Il possède également un compteur car, chacune des actions qu'il fait lui coût un point d'énergie
    Enfin, pour se déplacer et prendre des décisions, il doit connaitre son environnement
    """

    def __init__(self, board, energy=20):
        self.x = random.randint(0, 4)
        self.y = random.randint(0, 4)
        self.energy = energy
        self.board = board

    def move_up(self):
        self.y = self.y - 1

    def move_down(self):
        self.y = self.y + 1

    def move_right(self):
        self.x = self.x + 1

    def move_left(self):
        self.x = self.x - 1

    def __get_not_empty_room(self):
        not_empty_room = []
        for i in range(5):
            for j in range(5):
                if(self.board.get_board()[i][j] != 0):  # Si la pièce n'est pas vide
                    not_empty_room.append([i, j])

        return not_empty_room

    def select_nearest_not_empty_room(self):
        not_empty_room = self.__get_not_empty_room()
        if(len(not_empty_room) == 0): return -1
        else:
            for idx, room in enumerate(not_empty_room):
                _min = math.sqrt(math.pow(room[0] - self.x, 2) + math.pow(room[1] - self.y, 2))
                if(idx == 0 or _min < min): 
                    min = _min
                    index = idx

        return not_empty_room[index]

    def reach_selected_room(self, room_coord):
        # Info : Bug ici lors du déplacement vers la case la plus proche
        # Todo: Ajouter l'énergie
        if(room_coord == [self.x, self.y] or room_coord == -1): return
        else:
            if(room_coord[0] < self.x): self.move_left()
            else: self.move_right()

            if(room_coord[1] < self.y): self.move_up()
            else: self.move_down()

    # Todo: Ajouter le fait de nettoiyer la pièce ou de ramasser le bijou ou les deux