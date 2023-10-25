from pybricks.hubs import InventorHub
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.pupdevices import ColorSensor, Motor, UltrasonicSensor
from pybricks.robotics import DriveBase
from pybricks.tools import StopWatch, wait

from missions import *
# from missions_dj_roos import *
from calibration import *

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
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=92)

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

# Wait for imu to be calibrated.
while not hub.imu.ready():
    print("Waiting for imu to become ready ...")

# Get hub battery percentage.
current_voltage = robot.hub.battery.voltage()
battery_percentage = (current_voltage / BATTERY_MAX_VOLTAGE) * 100

print(f"Robot calibrated and ready - {round(battery_percentage, 2)}% charged")
print(f"left attachment motor angle: {left_attachment_motor.angle()} \nright attachment motor: {right_attachment_motor.angle()}")

# Menu index
min_index = 1
index = 1
max_index = 7

index_greater = False

# Prevent centre button from shutting down hub
hub.system.set_stop_button(None)

# Menu system
while True:
    # Set bluetooth button as stop button.
    hub.system.set_stop_button(Button.BLUETOOTH)
    
    # Navigate menu index with left and right buttons.
    if Button.RIGHT in hub.buttons.pressed():
        wait(DEFAULT_WAIT_AFTER_BUTTON_PRESSED)
        index += 1
        hub.speaker.beep(index * 100, 100)
        hub.light.on(Color.BLUE)
        if index > max_index:
            index = max_index
            hub.light.on(Color.RED)

    elif Button.LEFT in hub.buttons.pressed():
        wait(DEFAULT_WAIT_AFTER_BUTTON_PRESSED)
        index -= 1
        hub.speaker.beep(index * 100, 100)
        hub.light.on(Color.YELLOW)
        if index < min_index:
            index = min_index
            hub.light.on(Color.RED)
            hub.speaker.beep(250, 100)

    hub.display.number(index)

    # Check if the center button was pressed.
    if Button.CENTER in hub.buttons.pressed():
        # During a run, set the bluetooth button as the stop button.
        hub.system.set_stop_button(Button.BLUETOOTH)
        wait(DEFAULT_WAIT_AFTER_BUTTON_PRESSED)
        if index == 0:
            calibrate(robot)
        if index == 1:
            run_1(robot)
        elif index == 2:
            run_2(robot)
        elif index == 3:
            run_3(robot)
        elif index == 4:
            run_4(robot)
        elif index == 5:
            run_5(robot)
        elif index == 6:
            run_6(robot)
        elif index == 7:
            run_6B(robot)

        # Adding to the index after every mission
        if index < max_index + 1:
            index = index + 1
        else:
            index = max_index

        # Reset the stop button to none.
        hub.system.set_stop_button(None)
