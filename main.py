from turtle import Screen, Turtle
from paddle import Paddle
from mid_net import Net
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

net = Net()
l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "o")
screen.onkey(r_paddle.go_down, "l")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    # detecting collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 345 or ball.distance(l_paddle) < 50 and ball.xcor() < -345:
        ball.bounce_x()

    # detect missing paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.lscore_increase()

    # dercr l paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.rscore_increase()






screen.exitonclick()
