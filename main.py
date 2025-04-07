from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

# screen.onkey(right_paddle.go_up, "Up")
# screen.onkey(right_paddle.go_down, "Down")
# screen.onkey(left_paddle.go_up, "w")
# screen.onkey(left_paddle.go_down, "s")

# Right paddle controls
screen.onkeypress(right_paddle.start_moving_up, "Up")
screen.onkeyrelease(right_paddle.stop_moving_up, "Up")
screen.onkeypress(right_paddle.start_moving_down, "Down")
screen.onkeyrelease(right_paddle.stop_moving_down, "Down")

# Left paddle controls
screen.onkeypress(left_paddle.start_moving_up, "w")
screen.onkeyrelease(left_paddle.stop_moving_up, "w")
screen.onkeypress(left_paddle.start_moving_down, "s")
screen.onkeyrelease(left_paddle.stop_moving_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    # Move paddles based on movement flags
    if right_paddle.moving_up:
        right_paddle.go_up()
    if right_paddle.moving_down:
        right_paddle.go_down()
    if left_paddle.moving_up:
        left_paddle.go_up()
    if left_paddle.moving_down:
        left_paddle.go_down()

    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
