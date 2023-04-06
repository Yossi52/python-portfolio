from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)

    def go_right(self):
        new_x_pos = self.xcor() + 30
        self.goto(new_x_pos, self.ycor())

    def go_left(self):
        new_x_pos = self.xcor() - 30
        self.goto(new_x_pos, self.ycor())
