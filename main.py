from turtle import Screen, Turtle
from snake import Snake # Import python files
from food import Food, PowerUp, PowerDown
from scoreboard import Score
import random
import time

bg_colours = ["black", "pink", "green", "brown", "cyan"]
screen = Screen()
turtle = Turtle()
screen.tracer(0)
screen.setup(width=600, height =600)  # Sets the screen width and height
screen.bgcolor(random.choice(bg_colours))

turtle.hideturtle()
turtle.color("white")
turtle.write("Snake Game by Sulav Rai", align="center", font=("Arial", 30, "normal"))  # Shows the game name for 5 seconds
time.sleep(3)
turtle.clear()
turtle.write("Avoid the Black Turtle", align="center", font=("Arial", 30, "normal"))
time.sleep(2)
screen.title("Sulav's Snake Game")
turtle.clear()
game_is_on = True  # As long as this boolean value is "True", the game will continue to run
snake = Snake()  # class instantiation for the snake body, the food, and the score
food = Food()
score = Score()
golden_turtle = PowerUp()
black_turtle = PowerDown()

screen.onkey(snake.move_up, "w")  # control the Sketch using "wasd"
screen.onkey(snake.move_down, "s")
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_right, "d")


while game_is_on:
    time.sleep(0.1)  # Game updates every 0.1 seconds
    snake.move()
    screen.listen()
    screen.update()
    if snake.snake_body[0].distance(food) < 15:  # If the snake head touches the food, three methods are called
        food.refresh()  # This method spawns the food item in a another part of the screen
        snake.extend()  # This method extends the snake by 1 block
        score.scoreboard(1)  # This method increases the score by 1
        golden_turtle.respawn()
        black_turtle.respawn_blk()
        if (score.score % 5) == 0:
            screen.bgcolor(random.choice(bg_colours))
    if snake.snake_body[0].distance(golden_turtle) < 15:
        golden_turtle.respawn()
        score.scoreboard(5)
    if snake.snake_body[0].distance(black_turtle) < 15:  # If the black turtle is caught, you lose 5 points
        black_turtle.respawn_blk()
        score.scoreboard(-5)
    if score.score < 0:  # If your score falls below 0, the game ends
        game_is_on = False
        score.game_over()

    if snake.snake_body[0].xcor() > 280 or snake.snake_body[0].xcor() < -280 or snake.snake_body[0].ycor() > 280 or snake.snake_body[0].ycor() < -280:
        game_is_on = False   # If the snake touches one of the boundaries, this boolean value is set as "False" and the game ends
        score.game_over()  # This method shows the "game over" text

    for segment in snake.snake_body[1:]:
        if snake.snake_body[0].distance(segment) < 10:  # If any other the snake segments touch each other, the game ends
            game_is_on = False
            score.game_over()

screen.exitonclick()

