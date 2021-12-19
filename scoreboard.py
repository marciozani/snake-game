from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(position)
        self.__update()

    def add_points(self, points):
        self.score += points
        self.__update()

    def __update(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("Courier", 12, "normal"))

    def game_over(self):
        self.setposition((0, 0))
        self.write("Game Over", False, align="center", font=("Courier", 20, "normal"))
