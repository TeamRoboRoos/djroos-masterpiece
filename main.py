from pybricks.hubs import InventorHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.pupdevices import ColorSensor, Motor, UltrasonicSensor
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, wait

from core import DEFAULT_WAIT_TIME, Robot
from missions import run_1, run_1B, run_2, run_3, run_4

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
    left_sensor,
    right_sensor,
    drive_base,
)

print(robot)

# Menu index
min_index = 1
index = 2
max_index = 10

# Prevent centre button from shutting down hub
hub.system.set_stop_button(None)

# Menu system
while True:
    # Wait to prevent multiple button presses.
    wait(150)

    # Prevent left button from shutting down hub.
    hub.system.set_stop_button(None)

    # Navigate menu index with left and right buttons.
    if Button.RIGHT in hub.buttons.pressed():
        index += 1
        hub.speaker.beep(1000, 100)
        hub.light.on(Color.BLUE)
        if index > max_index:
            index = max_index
            hub.light.on(Color.RED)
            hub.speaker.beep(index * 250, 100)

    elif Button.LEFT in hub.buttons.pressed():
        index -= 1
        hub.light.on(Color.YELLOW)
        if index < min_index:
            index = min_index
            hub.light.on(Color.RED)
            hub.speaker.beep(index * 250, 100)

        hub.speaker.beep(700, 100)
    hub.display.number(index)

    # Check if the center button was pressed.
    if Button.CENTER in hub.buttons.pressed():
        # Set the left button as the stop button during mission runs.
        hub.system.set_stop_button(Button.LEFT)
        if index == 1:
            wait(DEFAULT_WAIT_TIME)
            run_1B(robot)
        elif index == 2:
            wait(DEFAULT_WAIT_TIME)
            run_2(robot)
        elif index == 3:
            wait(DEFAULT_WAIT_TIME)
            run_3(robot)
        elif index == 4:
            wait(DEFAULT_WAIT_TIME)
            run_4(robot, -120, -120)
