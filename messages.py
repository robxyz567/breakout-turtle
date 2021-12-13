from turtle import Turtle


class Message(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_message(self, message, position):
        self.clear()
        self.goto(position)
        self.write(arg=message, align="center", font=("Courier", 25, "bold"))

