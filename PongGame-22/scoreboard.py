import turtle

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score=0
        self.r_score=0
        self.update_score()

    def update_score(self):
        self.goto(-200, 200)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(200,200)
        self.write(self.r_score,align="center",font=("Courier",50,"normal"))

    def l_point_increase(self):
        self.l_score+=1
        self.clear()
        self.update_score()

    def r_point_increase(self):
        self.r_score += 1
        self.clear()
        self.update_score()



