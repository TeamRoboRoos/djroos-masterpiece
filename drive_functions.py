"""Robot driving functions.
"""

from core import *
from pybricks.tools import StopWatch, wait


def move(
    robot: Robot,
    distance,
    heading,
    constant_speed=None,
    max_speed=None,
    wait_after_move=True,
):
    """Move the robot forward and backwards.

    Uses a ramp speed function to accelerate to top speed then decelerate before stopping.

    :param robot: The robot instance.
    :param distance: The distance in mm. Positive is for forwards and negative for backwards.
    :param heading: The heading to move towards.
    :param constant_speed: Move at a constant speed if specified, otherwise use ramp speed.
    :param max_speed: The maximum speed for the ramp function.
    :param wait_after_move: Whether to wait for a bit after the move.
    """
    # Determine the top speed based on the distance. Use a lower top speed for
    # shorter distances which gives better accuracy. Longer distances can use
    # higher max speed since we have more time to slow down.
    applied_max_speed = max_speed if max_speed else _get_max_speed(distance)

    # Convert distance to absolute value for forwards and backwards movement.
    absolute_distance = abs(distance)
    # Split of the distance into 3 sections. First section will accelerate to
    # the max speed, second section will drive at the max speed, third section
    # will decellerate to stop.
    section_distance = absolute_distance / 3
    # Rest the drive base distance.
    robot.drive_base.reset()
    # Current distance at initial read will be 0 due to drive base reset.
    current_distance = robot.drive_base.distance()

    # Compare current distance with desired distance.
    # Note: negative distance is already converted to absolute value.
    while current_distance < absolute_distance:
        # Get the speed. If a constant speed is specified use that otherwise
        # use the ramp speed.
        speed = (
            constant_speed
            if constant_speed
            else _get_ramp_speed(
                applied_max_speed, current_distance, absolute_distance, section_distance
            )
        )

        # Get the current driving heading using a K factor to correct heading
        # based on the gyro to ensure we drive straight.
        angle = _get_kp_angle(robot.hub.imu.heading(), heading, speed)

        # Pass original distance value to sign function to return 1 or -1 to
        # multiply with speed value. This will determine forward(+) or
        # backwards(-) driving.
        robot.drive_base.drive(speed * _sign(distance), angle)

        # Read current distance but convert to absolute value to cater for
        # backwards driving.
        current_distance = abs(robot.drive_base.distance())
    robot.drive_base.stop()

    # Wait a bit after a move by default for better accuracy.
    if wait_after_move:
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


def turn_timed(robot: Robot, run_time, target_angle, tolerance=1, max_turn_speed=TURN_SPEED_FAST):
    """Turns the robot left or right for spesific amount of miliseconds.
    
    :param robot: The robot instance.
    :param run_time: The runtime in milliseconds.
    :param target_angle: The target angle to turn on.
    :param max_turn_speed: The maximum turn speed for the ramp function.
    :param tolerance: The target angle tolerance.

    """

    stopwatch = StopWatch()
    stopwatch.reset()
    stopwatch.resume()
    start_time = stopwatch.time()
    elapsed = stopwatch.time() - start_time

    heading = robot.hub.imu.heading()
    absolute_delta_angle = abs(target_angle - heading)

    # Determine the max turn speed based on the absolute delta angle
    applied_max_turn_speed = (
        max_turn_speed if max_turn_speed else _get_max_turn_speed(absolute_delta_angle)
    )

    error_angle = _short_turn_angle(robot, target_angle)

    while round(error_angle) not in range(-tolerance, tolerance) and elapsed < run_time:
        turn_rate = _get_ramp_turn(error_angle, applied_max_turn_speed)
        robot.drive_base.drive(0, turn_rate)
        error_angle = _short_turn_angle(robot, target_angle)
        elapsed = stopwatch.time() - start_time
    
    robot.drive_base.stop()


def turn(robot: Robot, target_angle, tolerance=1, max_turn_speed=TURN_SPEED_FAST):
    """Turn the robot to the target angle.

    Uses a ramp turn rate function to control the turn acceleration and deceleration.

    :param robot: The robot instance.
    :param target_angle: The target angle to turn on.
    :param tolerance: The target angle tolerance.
    :param max_turn_speed: The maximum turn speed for the ramp function.
    """
    # Get the current heading.
    heading = robot.hub.imu.heading()
    # Get the absolute angle the robot needs to turn, whether it is a left (-ve)
    # or right (+ve) turn.
    absolute_delta_angle = abs(target_angle - heading)

    # Determine the max turn speed based on the absolute angle. Small angles
    # use a lower turn speed for accuracy.
    applied_max_turn_speed = (
        max_turn_speed if max_turn_speed else _get_max_turn_speed(absolute_delta_angle)
    )

    # Determine the shortest angle to turn to in order to get to the target
    # angle. Error angle is how much left we need to turn.
    error_angle = _short_turn_angle(robot, target_angle)

    while round(error_angle) not in range(-tolerance, tolerance):
        # Get the turn turn speed based on how far the robot has turned.
        turn_rate = _get_ramp_turn(error_angle, applied_max_turn_speed)
        # Perform the turn.
        robot.drive_base.drive(0, turn_rate)
        # Get the error angle again after the turn.
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


def _get_max_speed(distance):
    return (
        DEFAULT_MAX_SPEED
        if distance >= LARGE_DISTANCE_THRESHOLD
        else DEFAULT_ACCURATE_SPEED
    )


def _get_max_turn_speed(absolute_delta_angle):
    return (
        DEFAULT_MAX_TURN_SPEED
        if absolute_delta_angle >= LARGE_ANGLE_THRESHOLD
        else DEFAULT_ACCURATE_TURN_SPEED
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


def _alternate_get_ramp_speed(
    max_speed,
    total_distance,
    current_distance,
    acceleration_factor=DEFAULT_ACCELERATION_FACTOR,
):
    first_third = total_distance / 3
    last_third = first_third * 2
    if current_distance == 0:
        return 20
    elif current_distance < first_third:
        return min(
            max_speed * ((current_distance / first_third) * acceleration_factor),
            max_speed,
        )
    elif current_distance > last_third:
        return min(
            (
                max_speed
                * ((total_distance - current_distance) / first_third)
                * acceleration_factor
            ),
            max_speed,
        )
    else:
        return max_speed


def _get_kp_angle(current_heading, target_heading, speed):
    kp_factor = -0.004 * speed + 4.2
    head = current_heading - target_heading
    return -head * kp_factor
