from turtle import Turtle


class Score(Turtle):  # Class inherits the turtle class
    def __init__(self):
        super().__init__()  # Initialises by creating a scoreboard
        self.score = 0
        with open("highscore.txt") as data:  # Opens the "highscore.txt" text file and reads the data
            self.high_score = int(data.read())  # The score in the text file is assigned to the "high_score" variable
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-125, 270)
        self.write(f"Score: {self.score} High Score {self.high_score}", align="left", font=("Arial", 16, "normal"))

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as data:  # If the high score record is broken, the text file is rewritten
                data.write(f"{self.high_score}")
        self.score = 0
        self.scoreboard(0)

    def scoreboard(self, point):  # This function increases the score by 1
        self.score = self.score + point
        self.clear()
        self.write(f"Score: {self.score} High Score {self.high_score}", align="left", font=("Arial", 16, "normal"))




