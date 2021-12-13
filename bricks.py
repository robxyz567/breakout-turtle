from turtle import Turtle

TRANSFER_CONST = 1000


class Bricks(Turtle):

    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(position)

    def transfer(self, direction):
        self.goto(self.xcor(), self.ycor() + direction*TRANSFER_CONST)

