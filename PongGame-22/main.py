import turtle as t
import paddle as p
import ball as b
import scoreboard as s
import time

screen=t.Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("plum1")
screen.title("PONG")
l_paddle=p.Paddle((-380,0))
r_paddle=p.Paddle((380,0))
ball=b.Ball()
score=s.Score()
screen.update()
screen.listen()
screen.onkeypress(key="Up",fun=r_paddle.upwards)
screen.onkeypress(key="Down",fun=r_paddle.downwards)
screen.onkeypress(key="w",fun=l_paddle.upwards)
screen.onkeypress(key="s",fun=l_paddle.downwards)
''' #onkey--> we can't keep it moving by pressing down on key, onkeypress--> we can!'''


game_over=False
while not game_over:
    time.sleep(ball.motion_speed)   #delay time. Bigger the num, more delay (slower)
    screen.update()
    ball.ball_move()
    if ball.ycor()>280 or ball.ycor()<-280:  #top 'n bottom walls
        ball.wall_bounce()

    if ball.distance(r_paddle)<50 or ball.distance(l_paddle)<50 :
        ball.paddle_bounce()
    '''w/o and ball.xcor()>360, the ball bounces multiple times n the paddle itself'''
    if ball.xcor()>380:
        ball.opp_side()
        score.l_point_increase()  #left gets point when right misses

    if ball.xcor() < -380:
        ball.opp_side()
        score.r_point_increase()


screen.exitonclick()
