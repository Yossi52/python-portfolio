from turtle import Turtle

COLORS = ["red", "red", "orange", "orange", "yellow", "yellow", "green", "green"]
BLOCK_YPOS = list(range(270, 70, -27))
BLOCK_XPOS = list(range(-270, 271, 60))


class Block():
    def __init__(self):
        self.all_blocks = []
        self.upper_bound = Turtle()
        self.upper_bound.hideturtle()
        self.upper_bound.pencolor("white")
        self.upper_bound.penup()
        self.upper_bound.goto(-300, 330)
        self.upper_bound.pendown()
        self.upper_bound.goto(300, 330)

    def create_block(self):
        for i in range(len(COLORS)):
            ypos = BLOCK_YPOS[i]
            for xpos in BLOCK_XPOS:
                new_block = Turtle()
                new_block.shape("square")
                new_block.shapesize(stretch_wid=0.9, stretch_len=2.7)
                new_block.color(COLORS[i])
                new_block.penup()
                new_block.goto(xpos, ypos)
                self.all_blocks.append(new_block)

    def collision_with_ball(self, ball):
        for block in self.all_blocks:
            if (block.xcor()-38 < ball.xcor() < block.xcor()+38) and (block.ycor()-20 < ball.ycor() < block.ycor()+20):
                block.goto(500, 500)
                self.all_blocks.pop(self.all_blocks.index(block))
                return True
