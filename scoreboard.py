from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        with open("data.txt") as self.data:
            self.high_score = int(self.data.read())
        self.score = 0
        self.update_scoreboard()

    def score_point(self):
        self.score += 1


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 16, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as self.data:
                self.data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()





