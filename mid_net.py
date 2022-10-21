from turtle import Turtle

class Net(Turtle):
    def __init__(self):
        super(Net, self).__init__()
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        self.color("white")
        self.hideturtle()
        self.dot()
        self.pendown()
        self.speed("fastest")
        self.goto(0, 300)
