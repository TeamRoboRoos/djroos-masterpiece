from drive_functions import hold, move_distance, move_until_black_line, turn

def mission_1(robot):
    move_distance(robot, 2000, 500, 10)

def mission_2(robot):
    move_until_black_line(robot, 150, 10)
