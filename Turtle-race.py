import turtle as t
import random

screen=t.Screen()
screen.setup(width=500,height=400)
game_start=False
all_turtles=[]
colours=['purple','blue','yellow','orange','green yellow','light coral']
position=[-70,-30, 0,30,70,100]
users_choice=screen.textinput(prompt="Who would win the race?purple/blue/yellow/orange/green yellow/light coral  :", title="MAKE A BET!").lower()
for turtle_guy in range(6):
    tim= t.Turtle(shape="turtle")
    tim.penup()
    tim.color(colours[turtle_guy])  #accesses value @ index
    tim.goto(x=-230, y=position[turtle_guy])
    all_turtles.append(tim)

if users_choice: #i.e has user given input. If yes-->True. hence "if" executes code
    game_start=True
while game_start:
    for little_turtle in all_turtles:
        '''width=500...500/2=250...but the turtle icon dimension is 20x20 px.....250-20=230...
        therefore if turtle has reached an x coordinate greater than 230, we can declare it winner
        w/o having to wait for it to reach full 250'''
        if little_turtle.xcor()>230:
            game_start=False
            winning_color=little_turtle.pencolor()  #Return or set the pencolor.
            if winning_color==users_choice:
                print("You have won")
            else:
                print("You have lost")
            print(f"The winning color is {winning_color}")
        random_distance_to_move=random.randint(0,6)
        little_turtle.forward(random_distance_to_move)



screen.exitonclick()
