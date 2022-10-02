from turtle import Turtle
from food import Food

FONT=("Courier", 20, "normal")
ALIGN = "center"


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score= 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.color("white")
        self.score_update()


    def score_update(self):
        self.clear()
        self.write(f"Score = {self.score} High Score : {self.highscore}",align= ALIGN,font = FONT)


    def reset(self):
        if self.score>self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.score_update()
    def score_increase(self):
        self.score +=1
        self.score_update()