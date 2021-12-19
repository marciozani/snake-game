from turtle import Turtle

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

STEP_SIZE = 20


class Snake:
    def __init__(self, size, initial_position):
        self.body = []
        self.__create_snake(size, initial_position)
        self.head = self.body[0]

    def __append_tail(self, position):
        square = Turtle(shape="square")
        square.penup()
        square.color("white")
        square.goto(position)
        self.body.append(square)

    def __create_snake(self, size, initial_position):
        for i in range(size):
            position = initial_position[0] * i * -STEP_SIZE, initial_position[1]
            self.__append_tail(position)
            # square = Turtle(shape="square")
            # square.penup()
            # square.color("white")
            # square.goto(initial_position[0] * i * -STEP_SIZE, initial_position[1])
            # self.body.append(square)

    def eat(self):
        self.__append_tail(self.body[-1].position())

    def move(self):
        last_position = self.head.position()
        self.head.forward(STEP_SIZE)
        for i in range(1, len(self.body)):
            position = self.body[i].position()
            self.body[i].setposition(last_position)
            last_position = position

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
