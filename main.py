import turtle

tim = turtle.Turtle()
screen = turtle.Screen()
def move_forward():
    tim.forward(15)

def move_backword():
    tim.backward(15)

def move_CounterClockWise():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)

def move_clockwise():
    new_heading= tim.heading()-10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()

screen.listen()
screen.onkey(key='d',  fun=move_clockwise)
screen.onkey(key='a',  fun=move_CounterClockWise)
screen.onkey(key='s',  fun=move_backword)
screen.onkey(key='w',  fun=move_forward)
screen.onkey(key='c',  fun=clear)




screen.exitonclick()