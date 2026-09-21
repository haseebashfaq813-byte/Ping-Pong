from turtle import Turtle

class Centreline(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.goto(0,350)
        self.goto(0,-350)

class Paddle(Turtle):
    def __init__(self,color, position):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
