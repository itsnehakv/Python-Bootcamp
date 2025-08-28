import turtle
class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.x_move=10
        self.y_move=10
        self.motion_speed=0.1

    def ball_move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def wall_bounce(self):
        self.y_move*=-1   #y_move=-10, x keeps increasing, y keeps decreasing

    def paddle_bounce(self):
        self.x_move*=-1
        self.motion_speed*=0.9 #reduce value (bcs decimal) but makes sure it does not go into -ve values


    def opp_side(self):
        self.goto(0,0)
        self.motion_speed = 0.1 #when ball reset, speed reset
        self.paddle_bounce()



