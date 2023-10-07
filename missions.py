from drive_functions import hold, move_distance, turn

def mission_1(hub, drive_base, left_motor, right_motor):
    move_distance(hub, drive_base, 2000, 500, 10)
    hold(left_motor, right_motor)
