from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()  # Initialises by creating a food item
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")

        self.speed("fastest")
        self.refresh()

    def refresh(self):  # This function spawns a food item at a random point in the screen
        self.goto(random.randint(-280, 280), random.randint(-280, 280))


class PowerUp(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(2, 2)
        self.color("gold")
        self.speed("fastest")
        self.hideturtle()
        self.respawn()

    def respawn(self):  # The turtle has a 35% chance of appearing and gives 5 points is caught
        if random.randint(0, 100) < 35:
            self.goto(random.randint(-280, 280), random.randint(-280, 280))
            self.showturtle()
        else:
            self.hideturtle()
            self.goto(300, 300)


class PowerDown(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(2, 2)
        self.color("black")
        self.pencolor("red")
        self.speed("fastest")
        self.hideturtle()
        self.respawn_blk()

    def respawn_blk(self):  # The turtle has a 35% chance of appearing and gives 5 points is caught
        if random.randint(0, 100) < 35:
            self.goto(random.randint(-280, 280), random.randint(-280, 280))
            self.showturtle()
        else:
            self.hideturtle()
            self.goto(300, 300)


