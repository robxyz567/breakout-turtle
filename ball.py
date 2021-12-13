from turtle import Turtle

MOVE_CONSTANT = 5
STARTING_SPEED = 0.015


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = MOVE_CONSTANT
        self.y_move = MOVE_CONSTANT
        self.move_speed = STARTING_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_vertical(self):
        self.y_move *= -1

    def bounce_horizontal(self):
        self.x_move *= -1

    def miss(self):
        self.goto(0, 0)

