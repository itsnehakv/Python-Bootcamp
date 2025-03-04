STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

import turtle as t

class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)  #or self.at_finish_line()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def at_finish_line(self):
        self.goto(STARTING_POSITION)
