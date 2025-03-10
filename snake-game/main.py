import turtle as t
import snake as s
import food as f
import scoreboard as sb
import time

screen=t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Welcome to the iconic snake game!")
screen.tracer(0)

snake=s.Snake()
food=f.Food()
scoreboard=sb.Scoreboard()

screen.listen()
screen.onkey(key="Up",fun=snake.upwards)
screen.onkey(key="Down",fun=snake.downwards)
screen.onkey(key= "Right",fun=snake.rightwards)
screen.onkey(key="Left",fun=snake.leftwards)

game_over=False
while not game_over:
    screen.update()
    time.sleep(0.1)

    snake.move() #snake will keep on moving forward, while the program/screen "listens" for keypresses.The move() method is constant & always executing

    if snake.head.distance(food) < 15:
       snake.extend()
       food.refresh()
       scoreboard.calculate_score()
    '''#distance() calculates distance b/w the turtle (here head of snake) and the food object. 
       # the food obj is 10x10 px. 
        If distance b/w head & food is less than 15 px'''

    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290: #notice >, <
        scoreboard.reset()
        snake.reset()

    for body in snake.our_snake[1:]:  #except head
        if snake.head.distance(body) < 10: #if snake hits itself
            scoreboard.reset()


screen.exitonclick()
