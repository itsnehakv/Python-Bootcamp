import turtle as t
MOVE_BY=10
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.our_snake=[]
        self.create_snake()
        self.head=self.our_snake[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.adding_segments(position)


    def adding_segments(self,position):
        tim = t.Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.our_snake.append(tim)

    def extend(self):
        self.adding_segments(self.our_snake[-1].position()) #here position() is a turtle method. our_snake[-1] fetches the tail position

    def move(self):
        for snake in range(len(self.our_snake)-1,0,-1): #(3-1,0.-1) ==> 2,0,-1 ==>only 2,1 basically. -1 step(goes backward)
             new_x=self.our_snake[snake-1].xcor()
             new_y = self.our_snake[snake - 1].ycor()
             self.our_snake[snake].goto(new_x,new_y)

        self.head.forward(MOVE_BY)   #head moves forward, rest try catching up to it

    def upwards(self):
        if self.head.heading()!=DOWN:    #bcs in actual snake game we can't go up & then down (can't backtrack). Same w/ left n right
           self.head.setheading(90)


    def downwards(self):
        if self.head.heading()!=UP:
            self.head.setheading(270)

    def leftwards(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(180)

    def rightwards(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(0)

    def reset(self):
        for body in self.our_snake:
            body.goto(1000,1000)
        self.our_snake.clear()
        self.create_snake()
        self.head=self.our_snake[0]   #must be initialized again after death

    ''''when the snake is clear()ed, it still remains on screen but dead. 
    To avoid this, it is made to go to (1000,1000) which is way more than our screen setup'''
