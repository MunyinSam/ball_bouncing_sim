import turtle

def move_up():
    target_angle = 90
    turn_to(target_angle)
    turtle.forward(10)

def move_left():
    target_angle = 180
    turn_to(target_angle)
    turtle.forward(10)

def move_right():
    target_angle = 0
    turn_to(target_angle)
    turtle.forward(10)

def move_down():
    target_angle = 270
    turn_to(target_angle)
    turtle.forward(10)

def turn_to(target_angle):
    current_angle = turtle.heading()
    turn_angle = target_angle - current_angle

    if turn_angle > 180:
        turn_angle -= 360
    elif turn_angle < -180:
        turn_angle += 360

    turtle.left(turn_angle)

turtle.onkey(move_up, "Up")
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_down, "Down")

turtle.listen()
turtle.done()
