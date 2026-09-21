from turtle import Screen, Turtle
from paddles import Paddle,Centreline
from ball import Ball
from score import Scoreboard
import time

turtle = Turtle()

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
centre = Centreline()

r_paddle = Paddle("green",(350, 0))
l_paddle = Paddle("blue",(-350, 0))
ball = Ball()
scoreboard = Scoreboard()

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

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle and l_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score >= 5:
        ball.reset_position()
        game_is_on = False
        screen.clear()
        screen.bgcolor("black")
        turtle.color("blue")
        turtle.write("PLAYER 1 WON!!!!", align="center", font=("ComicSans MS", 50, "normal"))
    elif scoreboard.r_score >= 5:
        ball.reset_position()
        game_is_on = False
        screen.clear()
        screen.bgcolor("black")
        turtle.color("green")
        turtle.write("PLAYER 2 WON!!!!", align="center", font=("ComicSans", 50, "normal"))


screen.exitonclick()
