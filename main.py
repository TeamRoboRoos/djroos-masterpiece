from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from attachment_functions import reset_motors
from hub_functions import countdown
from missions import (
    run_1,
    run_2,
    run_3,
    run_4,
    mission_1,
    mission_2,
    test_rotation,
    reset_attachment_motors,
    rotate_both_motors)

# Robot class
class Robot:
    def __init__(
        self,
        hub: InventorHub,
        left_motor: Motor,
        right_motor: Motor,
        left_attachment_motor: Motor,
        right_attachment_motor: Motor,
        left_sensor: ColorSensor,
        right_sensor: ColorSensor,
        drive_base: DriveBase
    ):
        self.hub = hub
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.left_attachment_motor: Motor = left_attachment_motor
        self.right_attachment_motor = right_attachment_motor
        self.left_sensor = left_sensor
        self.right_sensor = right_sensor
        self.drive_base = drive_base

# Initialise hub
hub = InventorHub()

# Initialise drive motors
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, reset_angle=True)
right_motor = Motor(Port.E, reset_angle=True)

# Initialise attachment motors
left_attachment_motor = Motor(Port.D)
right_attachment_motor = Motor(Port.F)

# Initialise sensors
left_sensor = ColorSensor(Port.A)
right_sensor = ColorSensor(Port.B)

# Initialise drive base
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=60, axle_track=90)

# Initialise robot
robot = Robot(
    hub,
    left_motor,
    right_motor,
    left_attachment_motor,
    right_attachment_motor,
    left_sensor, right_sensor,
    drive_base)

# Lspeed, Lacceleration, Ltorqe = left_motor.control.limits()
# Rspeed, Racceleration, Rtorqe = right_motor.control.limits()

# left_motor.control.limits(Lspeed, (Lacceleration, Lacceleration/2), Ltorqe)
# right_motor.control.limits(Rspeed, (Racceleration, Racceleration/2), Rtorqe)

# Lspeed, Lacelretion, Ltorqe = left_attachment_motor.control.limits()
# left_motor.control.limits(Lspeed, Lacelretion, Ltorqe)
# Rspeed, Racelretion, Rtorqe = right_attachment_motor.control.limits()
# right_attachment_motor.control.limits(Rspeed, Racelretion, Rtorqe)

# Menu index
min_index = 1
index = 1
max_index = 10

# Prevent centre button from shutting down hub
hub.system.set_stop_button(None)

reset_motors(robot, 0)

# Menu system
while True:
    if Button.RIGHT in hub.buttons.pressed():
        index += 1
        hub.speaker.beep(1000, 100)
        hub.light.on(Color.BLUE)
        if index > max_index:
            index = max_index
            hub.light.on(Color.RED)
            hub.speaker.beep(100, 100)

        wait(250)
    elif Button.LEFT in hub.buttons.pressed():
        index -= 1
        hub.light.on(Color.YELLOW)
        if index < min_index:
            index = min_index
            hub.light.on(Color.RED)
            hub.speaker.beep(100, 100)

        wait(250)
        hub.speaker.beep(700, 100)
    hub.display.number(index)

    if Button.CENTER in hub.buttons.pressed() and index == 1:
        print(hub.buttons.pressed())
        wait(750)
        run_1(robot)
        #reset_attachment_motors(robot, 10)
    elif Button.CENTER in hub.buttons.pressed() and index == 2:
        wait(750)
        # run_2(robot)
        run_2(robot)
    elif Button.CENTER in hub.buttons.pressed() and index == 3:
        wait(750)
        run_3(robot)
    elif Button.CENTER in hub.buttons.pressed() and index == 4:
        wait(750)
        run_4(robot, -120, -120)
    elif Button.BLUETOOTH in hub.buttons.pressed() and Button.CENTER in hub.buttons.pressed() or Button.CENTER in hub.buttons.pressed() and Button.BLUETOOTH in hub.buttons.pressed():
        hub.system.shutdown()