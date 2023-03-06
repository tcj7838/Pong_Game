from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WALL_UP = 280
WALL_DOWN = -280
SPEED_UP_VALVE = 5
WINNER_SCORE = 3
SLEEP_TIME = 0.08


def new_round():
    """開啟新局"""
    ball.serve()
    player_1.reset_position()
    player_2.reset_position()


def play_game():
    # 循環中會調用的變數
    game_is_on = True
    num_of_hit_paddle = 0
    sleep_time = SLEEP_TIME
    hit_paddle_switch_on = True

    scoreboard.new_game()
    new_round()

    while game_is_on:
        time.sleep(sleep_time)
        screen.update()
        ball.move()

        if ball.ycor() > WALL_UP or ball.ycor() < WALL_DOWN:
            ball.hit_wall()

        if -30 < ball.xcor() < 30:
            hit_paddle_switch_on = True

        # 撞擊paddle判定與角度調整
        if player_1.distance(ball) < 2600**0.5 and -380 < ball.xcor() < -355 and hit_paddle_switch_on:
            ball.hit_l_paddle(player_1.ycor())
            hit_paddle_switch_on = False
            num_of_hit_paddle += 1
            print(ball.heading())
        elif player_2.distance(ball) < 2600**0.5 and 380 > ball.xcor() > 355 and hit_paddle_switch_on:
            ball.hit_r_paddle(player_2.ycor())
            hit_paddle_switch_on = False
            num_of_hit_paddle += 1
            print(ball.heading())

        # 球加速(減少延遲時間)
        if num_of_hit_paddle == SPEED_UP_VALVE:
            sleep_time *= 0.8
            num_of_hit_paddle = 0

        # 開起新局(出界判定、得分、球位置、槳位置重置)
        if ball.xcor() < -400 or ball.xcor() > 400:
            if ball.xcor() < -400:
                scoreboard.get_point("P2")
            else:
                scoreboard.get_point("P1")
            new_round()
            num_of_hit_paddle = 0
            sleep_time = SLEEP_TIME

        # 遊戲結束宣布贏家
        if scoreboard.p1_score == WINNER_SCORE or scoreboard.p2_score == WINNER_SCORE:
            game_is_on = False
            if scoreboard.p1_score == WINNER_SCORE:
                scoreboard.game_over(1)
            else:
                scoreboard.game_over(2)


# 窗口設置
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

# 創造paddle, ball, scoreboard
player_1 = Paddle("left")
player_2 = Paddle("right")
ball = Ball()
scoreboard = Scoreboard()

# 動作監聽 - player的上下移動
screen.listen()
screen.onkey(fun=player_1.up, key="w")
screen.onkey(fun=player_1.down, key="s")
screen.onkey(fun=player_2.up, key="Up")
screen.onkey(fun=player_2.down, key="Down")
screen.onkey(fun=play_game, key="y")

# 遊戲開始
play_game()

screen.exitonclick()
