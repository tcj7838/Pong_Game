from turtle import Turtle, Screen
LEFT = -380
RIGHT = 380
MOVING_DISTANCE = 30


class Paddle(Turtle):

    def __init__(self, side):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        if side == "left":
            self.goto(LEFT, 0)
        else:
            self.goto(RIGHT, 0)
        self.ready_play = self.position()

    def reset_position(self):
        self.goto(self.ready_play)

    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVING_DISTANCE)

    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVING_DISTANCE)


if __name__ == "__main__":
    screen = Screen()
    screen.setup(800, 600)
    screen.bgcolor("black")
    screen.screensize(canvwidth=600, canvheight=800)

    test = Paddle("left")
    test2 = Paddle("right")

    screen.exitonclick()