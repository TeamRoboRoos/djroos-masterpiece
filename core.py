from pybricks.hubs import InventorHub
from pybricks.parameters import Stop
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase

# If the distance is greater than this amount then regard this as a large distance.
LARGE_DISTANCE_THRESHOLD = 600

# If the angle is greater than this amount then regard this as a large angle.
LARGE_ANGLE_THRESHOLD = 60

# The max drive speed to use for large distances.
DRIVE_SPEED_FAST = 500

# The max drive speed to use for smaller distances.
DRIVE_SPEED_ACCURATE = 300

# The max turn speed to use for larger angles.
TURN_SPEED_FAST = 340

# The max turn speed to use for smaller angles.
TURN_SPEED_ACCURATE = 100

# The minimum turn speed
MIN_TURN_SPEED = 10

# The default time to wait after a move.
DEFAULT_WAIT_AFTER_MOVE = 100

# The default time to wait after a button press.
DEFAULT_WAIT_AFTER_BUTTON_PRESSED = 500

# The default speed for rotating attachments.
DEFAULT_ATTACHMENT_SPEED = 250

# The default hold method for attachments.
DEFAULT_HOLD_METHOD = Stop.BRAKE

# The Inventor Hub max voltage to determine battery capacity.
BATTERY_MAX_VOLTAGE = 8320


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
        drive_base: DriveBase,
    ):
        self.hub = hub
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.left_attachment_motor: Motor = left_attachment_motor
        self.right_attachment_motor = right_attachment_motor
        self.left_sensor = left_sensor
        self.right_sensor = right_sensor
        self.drive_base = drive_base

    def reset_heading(self):
        self.hub.imu.reset_heading(0)

    def reset_distance(self):
        self.drive_base.reset()
