from turtle import Turtle
from car_manager import  CarManager

car_manager = CarManager()
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        x_cor = self.xcor()
        y_cor = self.ycor() + MOVE_DISTANCE
        self.goto(x_cor,y_cor)

    def is_at_finish_line(self):
        if (self.ycor() > FINISH_LINE_Y):
            return True
        else:
            return False

    def go_start_position(self):
        self.goto(STARTING_POSITION)