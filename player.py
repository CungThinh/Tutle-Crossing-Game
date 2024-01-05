from turtle import Turtle


class Player(Turtle):
    STARTING_POS = (0, -250)

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("Black")
        self.goto(self.STARTING_POS)
        self.setheading(90)

    def move(self):
        self.forward(20)

    def reset(self):
        self.goto(self.STARTING_POS)
