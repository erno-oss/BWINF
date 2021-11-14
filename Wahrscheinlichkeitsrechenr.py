import random


class MÄDN:

    def __init__(self, würfel, player_color):
        self.array = [i for i in range(41)]
        self.player_position = 0
        self.würfel = würfel
        self.player_color = player_color
        self.player_on_board = False
        self.player_in_base = False
        self.turns = 0

    def gehen(self, distanz):
        # if self.player_on_board is True and self.player_position + distanz < 41:
        self.player_position += distanz

    def auf_das_Spielfeld(self):
        for counter in range(3):
            if random.choice(self.würfel) == 6:
                self.player_on_board = True
                break


red1 = MÄDN([i for i in range(20)], "red")
red2 = MÄDN([1, 2, 3, 4, 5, 6])

players = [red1, red2]


while red1.player_on_board is False:
    red1.auf_das_Spielfeld()
    turns += 1
while red1.player_position < 42:
    red1.gehen(random.choice(red1.würfel))
    turns += 1

print(red1.player_on_board, red1.player_position, turns)
