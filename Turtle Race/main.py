from turtle import Turtle,Screen
import random
screen = Screen()

is_race_off = False
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a colour :")
colour = ["red","green","blue","black","yellow","orange"]
y_position = [-70,-40,-10,20,50,80]
all_turtles = []


for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colour[i])
    new_turtle.goto(x=-230, y=y_position[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_off = True

while is_race_off:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_off = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! {winning_color} is winner...")
            else:
                print(f"You have lost! {winning_color} is winner...")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()