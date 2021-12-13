from turtle import Turtle

MOVE_CONSTANT = 8


class Paddle(Turtle):

    def __init__(self, board_height):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.x_move = MOVE_CONSTANT
        self.goto(0, -0.45*board_height)

    def move(self, board_width):
        new_x = self.xcor() + self.x_move
        if new_x > board_width/2 or new_x < -board_width/2:
            self.x_move = -self.x_move
        self.goto(new_x, self.ycor())

    def left(self):
        self.x_move = -MOVE_CONSTANT

    def right(self):
        self.x_move = MOVE_CONSTANT