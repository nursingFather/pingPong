from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 280)
        self.write(f"p1 score: {self.l_score}")
        self.goto(200, 280)
        self.write(f"p2 score: {self.r_score}")

    def lscore_increase(self):
        self.l_score += 1
        self.update_scoreboard()

    def rscore_increase(self):
        self.r_score += 1
        self.update_scoreboard()