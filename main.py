from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

current_snake = []

x_postion = 0
for num in range(1,4):
    new_snake = Turtle()
    new_snake.color("white")
    new_snake.shape("square")
    new_snake.penup()
    new_snake.goto(x_postion, 0)
    current_snake.append(new_snake)
    x_postion += -20

print(current_snake[2].position())

# Get each segment to start moving forward on its own.
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(.25)
    for seg_num in range(len(current_snake) - 1, 0, -1):
    #The range starts at (2, 0, -1)
        new_x = current_snake[seg_num - 1].xcor()
        # = current_snake[1].xcor() ---> (-20, 0)
        new_y = current_snake[seg_num - 1].ycor()
        # = current_snake[1].ycor() ---> (0, 0)
        current_snake[seg_num].goto(new_x, new_y)
        # current_snake[2].goto(-20, 0)
        # This moves the third box to the current position of the second box
        # This will then repeat the process
    current_snake[0].forward(20)






















screen.exitonclick()
