from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("Black")
        self.penup()
        self.goto(x=-230, y=260)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))
        self.hideturtle()

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))