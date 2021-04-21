from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.current_snake = []
        self.create_snake()
        self.head = self.current_snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle()
            new_segment.color("white")
            new_segment.shape("square")
            new_segment.penup()
            new_segment.goto(position)
            self.current_snake.append(new_segment)

    def move(self):
        for seg_num in range(len(self.current_snake) - 1, 0, -1):
        #The range starts at 2, ends at 0, and goes down by -1  (2, 0, -1)
            new_x = self.current_snake[seg_num - 1].xcor()
            # = current_snake[1].xcor() ---> (-20, 0)
            # This is the current x coordinate of the second snake segment
            new_y = self.current_snake[seg_num - 1].ycor()
            # = current_snake[1].ycor() ---> (0, 0)
            # This is the current y coordinate of the second snake segment
            self.current_snake[seg_num].goto(new_x, new_y)
            # current_snake[2].goto(-20, 0)
            # This moves the third box to the current position of the second box
            # This will then repeat the process
        self.current_snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
