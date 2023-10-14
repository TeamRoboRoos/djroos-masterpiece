from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from hub_functions import countdown
from core import Robot
from missions import (
    run_1,
    run_1B,
    run_2,
    run_3,
    run_4,
    test_rotation,
    reset_attachment_motors)

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

print(robot)

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
index = 2
max_index = 10

# Prevent centre button from shutting down hub
hub.system.set_stop_button(None)

# Menu system
while True:
    wait(150)
    if Button.RIGHT in hub.buttons.pressed():
        index += 1
        hub.speaker.beep(1000, 100)
        hub.light.on(Color.BLUE)
        if index > max_index:
            index = max_index
            hub.light.on(Color.RED)
            hub.speaker.beep(index*250, 100)

    elif Button.LEFT in hub.buttons.pressed():
        index -= 1
        hub.light.on(Color.YELLOW)
        if index < min_index:
            index = min_index
            hub.light.on(Color.RED)
            hub.speaker.beep(index*250, 100)

        hub.speaker.beep(700, 100)
    hub.display.number(index)

    if Button.CENTER in hub.buttons.pressed() and index == 1:
        wait(750)
        run_1B(robot)
    elif Button.CENTER in hub.buttons.pressed() and index == 2:
        wait(750)
        run_2(robot)
    elif Button.CENTER in hub.buttons.pressed() and index == 3:
        wait(750)
        run_3(robot)
    elif Button.CENTER in hub.buttons.pressed() and index == 4:
        wait(750)
        run_4(robot, -120, -120)
    elif Button.BLUETOOTH in hub.buttons.pressed():
        hub.system.shutdown()