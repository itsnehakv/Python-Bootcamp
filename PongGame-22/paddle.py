import turtle as t
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.our_paddles=[]
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=3, stretch_len=1)
        self.goto(position)

    def upwards(self):
        new_y=self.ycor()+25
        self.goto(self.xcor(),y=new_y)

    def  downwards(self):
        new_y=self.ycor()-25
        self.goto(self.xcor(),y=new_y)




