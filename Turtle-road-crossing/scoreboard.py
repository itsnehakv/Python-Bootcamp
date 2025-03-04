FONT = ("Courier", 24, "normal")
import turtle as t

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-370,260)
        self.level=1
        self.write(f"LEVEL:{self.level}",align="left",font=FONT)


    def level_up(self):
        self.level+=1
        self.clear()
        self.write(f"LEVEL:{self.level}",align="left",font=FONT)

    def when_game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center",font=FONT)
