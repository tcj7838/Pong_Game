from turtle import Turtle, Screen
from random import randint

ANGLE_MODIFY = 30


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.speed("fastest")
        self.penup()
        self.serve()

    def move(self):
        self.fd(10)

    def hit_wall(self):
        self.setheading(360 - self.heading())

    def hit_l_paddle(self, l_paddle_ycor):
        """撞擊左邊paddle後使球更改為計算後的角度"""
        change = (self.ycor() - l_paddle_ycor) / 50 * ANGLE_MODIFY
        # output == -90 ~ 90
        if self.heading() > 180:
            new_heading = max((540 - self.heading()) + change, 295)
        else:
            new_heading = min((180 - self.heading()) + change, 65)
        self.setheading(new_heading)

    def hit_r_paddle(self, r_paddle_ycor):
        """撞擊右邊paddle後使球更改為計算後的角度"""
        change = (self.ycor() - r_paddle_ycor) / 50 * ANGLE_MODIFY
        if self.heading() > 180:
            new_heading = min((540 - self.heading()) - change, 245)
            self.setheading(new_heading)
        else:
            new_heading = max((180 - self.heading()) - change, 115)
        self.setheading(new_heading)

    def serve(self):
        """發球，角度隨機指定"""
        self.goto(0, 0)
        angle = 90
        while 80 < angle < 100 or 260 < angle < 280:
            angle = randint(0, 359)
        self.setheading(angle)


if __name__ == "__main__":
    screen = Screen()
    screen.bgcolor("black")
    screen.screensize(canvwidth=600, canvheight=800)

    test = Turtle()
    test.color("white")
    test.setheading(-45)
    test.fd(50)

    screen.exitonclick()