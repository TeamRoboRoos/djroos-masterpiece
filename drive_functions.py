"""Robot driving functions.
"""

from core import (
    DEFAULT_DRIVE_SPEED,
    DEFAULT_KP_LOOP_ITERATIONS,
    DEFAULT_KP_VALUE,
    DEFAULT_TURN_SPEED,
    Robot,
)


def drive_straight(robot: Robot, index, speed=DEFAULT_DRIVE_SPEED, kp=DEFAULT_KP_VALUE):
    """Drives straight using the gyro and a kp value.

    :param robot: The robot class.
    :param speed: The speed to drive at.
    :param kp: The kp value.
    """
    heading = robot.hub.imu.heading()
    if index != 0 and index % DEFAULT_KP_LOOP_ITERATIONS == 0:
        heading = -heading * kp
        print(f"Adjusting heaing by - {heading}")
    robot.drive_base.drive(speed, heading)


def move_distance(
    robot: Robot, distance, speed=DEFAULT_DRIVE_SPEED, kp=DEFAULT_KP_VALUE
):
    """Drives the robot a given distance.

    :param robot: The robot instance.
    :param distance: The distance to drive.
    :param speed: The speed to drive at.
    :param kp: The kp value.
    """
    # Reset the accumulated drive distance and heading.
    robot.drive_base.reset()
    robot.hub.imu.reset_heading(0)

    # Keep driving until distance is reached.
    index = 0
    while robot.drive_base.distance() < distance:
        drive_straight(robot, index, speed, kp)
        index += 1

    # Stop the robot.
    robot.drive_base.stop()


def move_backwards_distance(
    robot: Robot, distance, speed=DEFAULT_DRIVE_SPEED, kp=DEFAULT_KP_VALUE
):
    """Drives the robot backwards a given distance.

    :param robot: The robot instance.
    :param distance: The distance to drive.
    :param speed: The speed to drive at.
    :param kp: The kp value.
    """
    # Reset the accumulated drive distance and heading.
    robot.drive_base.reset()
    robot.hub.imu.reset_heading(0)

    # Negate the distance since we are driving backwards.
    while -robot.drive_base.distance() < distance:
        drive_straight(robot, -speed, kp)

    robot.drive_base.stop()


def move_until_black_line(robot: Robot, speed=DEFAULT_DRIVE_SPEED, kp=DEFAULT_KP_VALUE):
    """Move until both colour sensors detect a black line.

    :param robot: The robot instance.
    :param speed: The speed to drive at.
    :param kp: The kp value.
    """
    robot.left_sensor.lights.off()
    robot.right_sensor.lights.off()
    robot.drive_base.reset()

    while True:
        reflection1 = robot.left_sensor.reflection()
        reflection2 = robot.right_sensor.reflection()

        print(f"Sensor1 - {reflection1}")
        print(f"Sensor2 - {reflection2}")

        # Check if black line detected
        white_line_detected = reflection1 > 90 and reflection2 > 90
        black_line_detected = reflection1 < 16 and reflection2 < 15

        if white_line_detected:
            break
        else:
            drive_straight(robot, speed, kp)

        if black_line_detected:
            break
        else:
            drive_straight(robot, speed, kp)

    hold(robot)


def right_sensor_move_until_black_line(
    robot: Robot, speed=DEFAULT_DRIVE_SPEED, kp=DEFAULT_KP_VALUE
):
    """Move until right colour sensor detects a black line

    :param robot: The robot instance.
    :param speed: The speed to drive at.
    :param kp: The kp value.
    """
    robot.left_sensor.lights.off()
    robot.right_sensor.lights.off()
    robot.drive_base.reset()

    while True:
        reflection = robot.right_sensor.reflection()

        # Check if black line detected
        black_line_detected = reflection < 15

        if black_line_detected:
            break
        else:
            drive_straight(robot, speed, kp)

    hold(robot)


def turn_on_one_wheel(robot: Robot, angle, speed=DEFAULT_TURN_SPEED):
    """Turns the robot on one wheel.

    Turns on right wheel if the angle is greater than 0, otherwise turn on left wheel.

    :param robot: The robot instance.
    :param angle: The target angle.
    :param speed: The speed of the turn.
    """
    robot.hub.imu.reset_heading(0)
    right_turn = angle > 0

    if right_turn:
        while robot.hub.imu.heading() < angle:
            robot.left_motor.run(speed)

    else:
        while robot.hub.imu.heading() > angle:
            robot.right_motor.run(speed)

    hold(robot)


def turn(robot: Robot, angle, speed=DEFAULT_TURN_SPEED):
    """Turns the robot to the given angle.

    Turns right if the angle is greater than 0, otherwise turns left.

    :param robot: The robot instance.
    :param angle: The target angle.
    :param speed: The speed of the turn.
    """
    # Resetting both the angle and the heading variable of the robot
    robot.hub.imu.reset_heading(0)
    right_turn = angle > 0

    # Checks if the robot should turn right or left
    if right_turn:
        while robot.hub.imu.heading() < angle:
            robot.right_motor.run(-speed)
            robot.left_motor.run(speed)
    else:
        while robot.hub.imu.heading() > angle:
            robot.right_motor.run(speed)
            robot.left_motor.run(-speed)

    hold(robot)


def turn_accurate(robot: Robot, angle):
    # Reset the heading before turning.
    robot.hub.imu.reset_heading(0)

    # Perform the turn.
    robot.drive_base.turn(angle)

    # Check the heading.
    heading = robot.hub.imu.heading()

    # Determine correction angle.
    correction_angle = angle - heading

    # Correct the angle.
    robot.drive_base.turn(correction_angle)


def set_acceleration(robot: Robot, acceleration):
    (
        straight_speed,
        straight_acceleration,
        turn_rate,
        turn_acceleration,
    ) = robot.drive_base.settings()
    robot.drive_base.settings(
        straight_speed, acceleration, turn_rate, turn_acceleration
    )


def hold(robot):
    """Stops the robot by holding both motors.

    :param robot: The robot instance.
    """
    robot.left_motor.hold()
    robot.right_motor.hold()
