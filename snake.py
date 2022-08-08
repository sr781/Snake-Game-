from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]  # Game starts with three blocks and each snake block is 20x20


class Snake:

    def __init__(self):  # Initialises by creating the snake
        self.snake_body = []  # Stores the x and y coordinated of each snake
        self.snake_creator()

    def snake_creator(self):  # This function starts the game by creating the snake
        for seg_pos in STARTING_POS:
            self.add_segment(seg_pos)

    def add_segment(self, seg_pos): # This function adds a block on the last block of the existing snake
        square = Turtle("square")
        square.penup()
        square.color("white")
        square.goto(seg_pos)
        self.snake_body.append(square)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())  # This function provides the position of the last block

    def move(self):  # This function moves each block in the snake behind each other
        for segment_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment_num - 1].xcor()
            new_y = self.snake_body[segment_num - 1].ycor()
            self.snake_body[segment_num].goto(new_x, new_y)
        self.snake_body[0].forward(20)

    def move_up(self):  # These functions control the direction of the snake
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)  # This prevents the snake from going back on itself

    def move_down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def move_left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def move_right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)
