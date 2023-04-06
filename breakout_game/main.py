from turtle import Screen
from paddle import Paddle
from block import Block
from ball import Ball, BALL_SPEED
from scoreboard import Scoreboard
import time

BALL_SP_1 = 0.01
BALL_SP_2 = 0.02
BALL_SP_3 = 0.03

screen = Screen()
screen.setup(width=600, height=800)
screen.title("Breakout")
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle((0, -350))
blocks = Block()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle.go_right, "Right")
screen.onkeypress(paddle.go_left, "Left")

blocks.create_block()

game_is_on = True
break_cnt = 0
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # 공이 양측 벽에 닿았을 때
    if ball.xcor() >= 280 or ball.xcor() <= -280:
        ball.bounce_x()
    # 공이 위쪽 벽에 닿았을 때
    if ball.ycor() >= 310:
        ball.bounce_y()
    # 공이 막대와 닿았을 때
    ball_x_sign = abs(ball.x_move)//ball.x_move
    ball_y_sign = abs(ball.y_move)//ball.y_move
    if (- 330 > ball.ycor() > -341) and (paddle.xcor() - 60 < ball.xcor() < paddle.xcor() + 60):
        if ball.distance(paddle) < 20:
            ball.x_move = ball_x_sign * 3
            ball.y_move = ball_y_sign * 18
        elif ball.distance(paddle) < 30:
            ball.x_move = ball_x_sign * 5
            ball.y_move = ball_y_sign * 15
        elif ball.distance(paddle) < 40:
            ball.x_move = ball_x_sign * 8
            ball.y_move = ball_y_sign * 12
        else:
            ball.x_move = ball_x_sign * 10
            ball.y_move = ball_y_sign * 10
        ball.bounce_y()
    # 공이 블럭과 닿았을 때
    if blocks.collision_with_ball(ball):
        ball.bounce_y()
        scoreboard.score += 1
        scoreboard.update_scoreboard()
        break_cnt += 1
    # 공이 블럭을 부순 수에 따라 속도 증가
    if break_cnt > 25:
        ball.move_speed = BALL_SP_1
    elif break_cnt > 15:
        ball.move_speed = BALL_SP_2
    elif break_cnt > 5:
        ball.move_speed = BALL_SP_3
    # 공을 놓쳤을 때
    if ball.ycor() <= -380:
        time.sleep(1)
        ball.move_speed = BALL_SPEED
        break_cnt = 0
        ball.reset_position()
        scoreboard.life -= 1
        scoreboard.update_scoreboard()
    # 남은 목숨이 없을 때
    if scoreboard.life <= 0:
        scoreboard.game_over()
        game_is_on = False
    # 게임을 클리어 했을 때
    if len(blocks.all_blocks) == 0:
        scoreboard.game_clear()
        game_is_on = False


screen.exitonclick()
