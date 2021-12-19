from turtle import Turtle


class Food(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.shapesize(.3, .3, 0)
        self.setposition(position)


