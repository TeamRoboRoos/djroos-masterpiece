from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from missions import mission_1
from hub_functions import countdown

hub = InventorHub()

# Initialise motors
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)

# Initialise drive base
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=60, axle_track=90)

Lspeed, Lacceleration, Ltorqe = left_motor.control.limits()
Rspeed, Racceleration, Rtorqe = right_motor.control.limits()

left_motor.control.limits(Lspeed, (Lacceleration, Lacceleration/2), Ltorqe)
right_motor.control.limits(Rspeed, (Racceleration, Racceleration/2), Rtorqe)

# Menu index
min_index = 0
index = 0
max_index = 10

# Prevent centre button from shutting down hub
hub.system.set_stop_button(None)

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

    if Button.CENTER in hub.buttons.pressed() and index == 0:
        print(hub.buttons.pressed())
        wait(750)
        mission_1(hub, drive_base, left_motor, right_motor)
    elif Button.CENTER in hub.buttons.pressed() and index == 1:
        wait(750)
        mission_1(hub, drive_base, left_motor, right_motor)
    elif Button.CENTER in hub.buttons.pressed() and index == 2:
        wait(750)
        mission_1(hub, drive_base, left_motor, right_motor)
    elif Button.CENTER in hub.buttons.pressed() and index == 3:
        wait(750)
        mission_1(hub, drive_base, left_motor, right_motor)
    elif Button.BLUETOOTH in hub.buttons.pressed() and Button.CENTER in hub.buttons.pressed() or Button.CENTER in hub.buttons.pressed() and Button.BLUETOOTH in hub.buttons.pressed():
        hub.system.shutdown()