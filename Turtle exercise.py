import turtle
from turtle import Turtle, Screen
import random

timmy=Turtle()
timmy.shape("turtle")
timmy.color("#97B5DE")

turtle.colormode(255)
def pick_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_colours=(r,g,b)
    return random_colours
direction=[0,90,180,270,]


r=100
timmy.speed("fastest")
def draw_circle(gap_bw):
    for i in range(int(360/gap_bw)):
        '''ensures that no circle is drawn on top of another.
        Total no of circles will be 360/5=72 (int bcs it will return float value)'''

        timmy.color(pick_color())
        timmy.circle(r)
        timmy.setheading(timmy.heading()+gap_bw)

         #it is the angle. Sets   angle = current_angle + gap between each circle

draw_circle(5)
screen=Screen()
screen.exitonclick()
