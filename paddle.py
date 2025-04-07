from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        # Add movement flags
        self.moving_up = False
        self.moving_down = False

    # Methods to start and stop moving up
    def start_moving_up(self):
        self.moving_up = True

    def stop_moving_up(self):
        self.moving_up = False

    # Methods to start and stop moving down
    def start_moving_down(self):
        self.moving_down = True

    def stop_moving_down(self):
        self.moving_down = False

    def go_up(self):
        new_y = self.ycor() + 20
        if new_y < 250:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y > -250:
            self.goto(self.xcor(), new_y)
