import turtle as t
class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("high_score_data.txt") as data:
            self.high_score=int(data.read())
        self.hideturtle()  #a turtle arrow shows up w/o this
        self.penup()
        self.goto(0,270)
        self.print_score()


    def print_score(self):
        self.clear()
        self.write(f"Score:{self.score} |  High Score:{self.high_score}",align='center',font=("Times New Roman",15,'normal'))


    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("high_score_data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0  #reset for new game
        self.print_score()


    # def game_over(self):
    #     self.goto(0,0) #text aligned at 0,0
    #     self. write("Game Over", align="center", font=("Copperplate",20,'normal'))

    def calculate_score(self):
        self.score+=1
        self.print_score()
