import time
import random
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

SCREEN_LEFT = -280
SCREEN_RIGHT = 280
SCREEN_UP = 280
SCREEN_DOWN = -280

screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

end_game = False
snake = Snake(size=3, initial_position=(0, 0))

food_position = random.randint(SCREEN_LEFT, SCREEN_RIGHT), random.randint(SCREEN_DOWN, SCREEN_UP)

food = Food(food_position)
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_scoreboard = Scoreboard((0, 270))

while not end_game:
    time.sleep(0.1)

    snake.move()

    # collision with food
    distance = snake.head.distance(food)
    if distance < 20:
        snake.eat()
        food.setposition(random.randint(SCREEN_LEFT, SCREEN_RIGHT), random.randint(SCREEN_DOWN, SCREEN_UP))
        game_scoreboard.add_points(1)

    # collision with wall
    if snake.head.xcor() <= SCREEN_LEFT or snake.head.xcor() >= SCREEN_RIGHT \
       or snake.head.ycor() >= SCREEN_UP or  snake.head.ycor() <= SCREEN_DOWN:
        end_game = True

    # collision with the tail
    for tail_segment in snake.body[1:]:
        if snake.head.distance(tail_segment) < 10:
            tail_segment.color("red")
            end_game = True
            break

    screen.update()

game_scoreboard.game_over()

screen.exitonclick()
