def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_on_right():
        turn_left()
    elif right_is_clear():
        turn_right()
    elif wall_in_front():
        turn_right()
        move()
