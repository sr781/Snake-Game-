from turtle import Turtle


class Score(Turtle):  # Class inherits the turtle class
    def __init__(self):
        super().__init__()  # Initialises by creating a scoreboard
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.goto(-25, 270)
        self.write(f"Score: {self.score}", align="left", font=("Arial", 16, "normal"))

    def game_over(self):  # This function is called if the game ends
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))

    def scoreboard(self, point):  # This function increases the score by 1
        self.score = self.score + point
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=("Arial", 16, "normal"))


