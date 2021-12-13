from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from messages import Message
import time

BOARD_W = 900
BOARD_H = 600
BRICKS_COLORS = ["red", "orange", "yellow", "green", "blue", "violet"]
BRICKS_NUMBER = 14


def bricks_builder(current_y, current_color):

    x_brick_position = -BOARD_W/2+30
    for i in range(BRICKS_NUMBER):
        bricks.append(Bricks((x_brick_position, current_y), current_color))
        x_brick_position += 64


screen = Screen()
screen.setup(width=BOARD_W, height=BOARD_H)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle(BOARD_H)
ball = Ball()
level = Message()
lives = Message()
game_over = Message()
bricks = []
y_bricks_position = BOARD_H/2-75
for color in BRICKS_COLORS:
    bricks_builder(y_bricks_position, color)
    y_bricks_position -= 23

screen.listen()
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")

level_number = 1
game_is_on = True
while game_is_on:

    hit_bricks = 0
    lives_number = 5

    level.update_message(f"Level: {level_number}", (-BOARD_W/2+100, BOARD_H/2-50))
    lives.update_message(f"Lives: {lives_number}", (BOARD_W/2-100, BOARD_H/2-50))

    current_level = True
    while current_level:

        time.sleep(ball.move_speed)
        screen.update()

        ball.move()
        paddle.move(BOARD_W)

        if ball.ycor() > (BOARD_H/2-20):
            ball.bounce_vertical()
        elif ball.xcor() > (BOARD_W/2-20) or ball.xcor() < (-BOARD_W/2+20):
            ball.bounce_horizontal()
        elif (paddle.xcor()+45) > ball.xcor() > (paddle.xcor()-45) and ball.ycor() < (paddle.ycor()+20):
            ball.bounce_vertical()
        elif ball.ycor() < -BOARD_H/2:
            ball.miss()
            lives_number -= 1
            lives.update_message(f"Lives: {lives_number}", (BOARD_W/2-100, BOARD_H/2-50))
            if lives_number == 0:
                game_over.update_message("GAME OVER", (0, -BOARD_H/6))
                current_level = False
                game_is_on = False

        for brick in bricks:
            if (brick.xcor()+40) > ball.xcor() > (brick.xcor()-40) and (brick.ycor()+20) > ball.ycor() > (brick.ycor()-20):
                ball.bounce_vertical()
                brick.transfer(-1)
                hit_bricks += 1

        if hit_bricks == len(bricks):
            level_number += 1
            ball.move_speed *= 0.95
            ball.miss()
            for brick in bricks:
                brick.transfer(1)
            current_level = False


screen.exitonclick()