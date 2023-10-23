from drive_functions import *

DISTANCE_ERROR_THRESHOLD = 10
ANGLE_ERROR_THRESHOLD = 0.5


def calibrate(robot: Robot):
    robot.reset_heading()
    robot.reset_distance()

    _test_move(robot, 300, 0)
    _test_turn(robot, 45)
    _test_move(robot, 600, 45)
    _test_turn(robot, 135)


def _test_move(robot: Robot, target_distance, heading):
    print(f"Moving {target_distance} ...")
    move(robot, target_distance, heading)
    wait(1000)
    distance = robot.drive_base.distance()
    print(f"Distance - {distance}")
    distance_error = target_distance - distance
    print(f"Distance error - {distance_error}")
    if abs(distance_error) > DISTANCE_ERROR_THRESHOLD:
        robot.hub.speaker.beep()

    robot.reset_distance()


def _test_turn(robot: Robot, target_angle):
    print(f"Turning {target_angle} ...")
    turn(robot, target_angle)
    wait(1000)
    heading = robot.hub.imu.heading()
    print(f"Heading - {heading}")
    angle_error = target_angle - heading
    print(f"Angle error - {angle_error}")
    if abs(angle_error) > ANGLE_ERROR_THRESHOLD:
        robot.hub.speaker.beep()
