"""Robot driving functions.
"""

from core import *
from pybricks.tools import StopWatch, wait


def move(robot: Robot, distance, heading, constant_speed=None):
    """Move the robot forward and backwards.

    Uses a ramp speed function to accelerate to top speed then decelerate before stopping.

    :param robot: The robot instance.
    :param distance: The distance in mm. Positive is for forwards and negative for backwards.
    :param heading: The heading to move towards.
    :param constant_speed: Move at a constant speed if specified, otherwise use ramp speed.
    """
    # Determine the top speed based on the distance
    top_speed = _get_top_speed(distance)

    # create new variable to convert distance to absolute value
    absolute_distance = abs(distance)
    section_distance = absolute_distance / 3
    robot.drive_base.reset()
    # current distance at initial read will be 0 due to drive base reset
    current_distance = robot.drive_base.distance()

    # compare current distance with desired distance
    # (note negative distance is already converted to absolute value)
    while current_distance < absolute_distance:
        speed = (
            constant_speed
            if constant_speed
            else _get_ramp_speed(
                top_speed, current_distance, absolute_distance, section_distance
            )
        )

        angle = _get_kp_angle(robot.hub.imu.heading(), heading, speed)

        # pass original distance value to sign function to return 1 or -1 to
        # multiply with speed value to determine forward(+) or backward(-) drive
        robot.drive_base.drive(speed * _sign(distance), angle)

        # read current distance but convert to absolute value to cover for
        # backward drive for comparison with absolute distance value
        current_distance = abs(robot.drive_base.distance())
    robot.drive_base.stop()
    wait(DEFAULT_WAIT_AFTER_MOVE)


def move_timed(robot: Robot, run_time, heading, speed):
    """Moves the robot forwards or backwards at a constant speed for a given number of milliseconds.

    :param robot: The robot instance.
    :param run_time: The runtime in milliseconds.
    :param heading: The heading to move towards.
    :param speed: The speed to drive at. Positive speed is forwards, negative speed is backwards.
    """
    stopwatch = StopWatch()
    stopwatch.reset()
    stopwatch.resume()
    start_time = stopwatch.time()
    elapsed = stopwatch.time() - start_time

    while elapsed < run_time:
        angle = _get_kp_angle(robot.hub.imu.heading(), heading, speed)
        robot.drive_base.drive(speed, angle)
        elapsed = stopwatch.time() - start_time
    robot.drive_base.stop()
    wait(DEFAULT_WAIT_AFTER_MOVE)


def turn(robot: Robot, target_angle, tolerance=1, constant_turn_rate=None):
    """Turn the robot to the target angle.

    Uses a ramp turn rate function to control the turn acceleration and deceleration.

    :param robot: The robot instance.
    :param target_angle: The target angle to turn on.
    :param tolerance: The target angle tolerance.
    :param constant_turn_rate: Turn at a constant rate if specified, otherwise use ramp speed.
    """
    # Determine the delta angle
    heading = robot.hub.imu.heading()
    absolute_delta_angle = abs(target_angle - heading)

    # Determine the max turn speed based on the absolute delta angle
    max_turn_speed = _get_max_turn_speed(absolute_delta_angle)

    error_angle = _short_turn_angle(robot, target_angle)

    while round(error_angle) not in range(-tolerance, tolerance):
        turn_rate = (
            constant_turn_rate
            if constant_turn_rate
            else _get_ramp_turn(error_angle, max_turn_speed)
        )
        robot.drive_base.drive(0, turn_rate)
        error_angle = _short_turn_angle(robot, target_angle)
    robot.drive_base.stop()


def turn_on_one_wheel(robot: Robot, target_angle, tolerance=1, constant_turn_rate=None):
    """Turns the robot on one wheel.

    :param robot: The robot instance.
    :param target_angle: The target angle.
    :param tolerance: The target angle tolerance.
    :param constant_turn_rate: Turn at a constant rate if specified, otherwise use ramp speed.
    """
    # Determine the delta angle
    heading = robot.hub.imu.heading()
    absolute_delta_angle = abs(target_angle - heading)

    # Determine the max turn speed based on the absolute delta angle
    max_turn_speed = _get_max_turn_speed(absolute_delta_angle)

    error_angle = _short_turn_angle(robot, target_angle)

    # Determine left or right turn based on error angle.
    right_turn = error_angle > 0

    while round(error_angle) not in range(-tolerance, tolerance):
        turn_rate = (
            constant_turn_rate
            if constant_turn_rate
            else _get_ramp_turn(error_angle, max_turn_speed)
        )
        if right_turn:
            robot.left_motor.run(turn_rate)
        else:
            robot.right_motor.run(turn_rate)
        error_angle = _short_turn_angle(robot, target_angle)
    _hold(robot)


def _short_turn_angle(robot: Robot, angle):
    return (angle - robot.hub.imu.heading() + 180) % 360 - 180


def _get_ramp_turn(angle, max_turn_speed):
    return ((max_turn_speed - MIN_TURN_SPEED) / 180) * angle + MIN_TURN_SPEED * _sign(
        angle
    )


def _sign(num):
    return 1 if num >= 0 else -1


def _hold(robot):
    """Stops the robot by holding both motors.

    :param robot: The robot instance.
    """
    # robot.left_motor.brake()
    # robot.right_motor.brake()
    robot.left_motor.hold()
    robot.right_motor.hold()


def _get_top_speed(distance):
    return (
        DRIVE_SPEED_FAST
        if distance >= LARGE_DISTANCE_THRESHOLD
        else DRIVE_SPEED_ACCURATE
    )


def _get_max_turn_speed(absolute_delta_angle):
    return (
        TURN_SPEED_FAST
        if absolute_delta_angle >= LARGE_ANGLE_THRESHOLD
        else TURN_SPEED_ACCURATE
    )


def _get_ramp_speed(top_speed, current_distance, total_distance, section_distance):
    if current_distance < section_distance:
        return ((top_speed - 20) / section_distance) * current_distance + 20
    elif section_distance < current_distance < section_distance * 2:
        return top_speed
    else:
        return (-(top_speed - 20) / section_distance) * (
            current_distance - total_distance
        ) + 20


def _get_kp_angle(current_heading, target_heading, speed):
    kp_factor = -0.004 * speed + 4.2
    head = current_heading - target_heading
    return -head * kp_factor
