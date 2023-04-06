from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.life = 3
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(210, 350)
        self.write(f"Life: {self.life}", align="center", font=("Courier", 25, "bold"))
        self.goto(-210, 350)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 25, "bold"))

    def life_lose(self):
        self.life -= 1

    def game_over(self):
        self.goto(0, 0)
        self.pencolor("red")
        self.write("GAME OVER", align="center", font=("Courier", 30, "bold"))

    def game_clear(self):
        self.goto(0, 0)
        self.pencolor("white")
        self.write("YOU WIN!", align="center", font=("Courier", 30, "bold"))
