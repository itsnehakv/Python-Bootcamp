import  turtle as t
import random

class Food(t.Turtle):   #so that object of Food() will directly have Turtle() behaviours/qualities & the Food classes behaviours/qualities
    def __init__(self):
        super().__init__()
        self.shape("circle")  #e.g of method of Turtle class being modified
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) #normally==>20x20 px, now 10x10px
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 260)  # we don't want 300 bcs it's too close to wall
        random_y = random.randint(-280, 260)
        self.goto(x=random_x, y=random_y)
