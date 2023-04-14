from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # collision with upper wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect r paddle miss
    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.l_point()

    # detect l paddle miss
    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.r_point()

screen.exitonclick()
