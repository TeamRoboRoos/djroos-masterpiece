from pybricks.hubs import InventorHub
from pybricks.parameters import Stop
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase

DEFAULT_DRIVE_SPEED = 300
DEFAULT_ACCELERATION = 275
DEFAULT_TURN_SPEED = 150
DEFAULT_TURN_ACCELERATION = 100
DEFAULT_ATTACHMENT_SPEED = 250
DEFAULT_KP_VALUE = 3
DEFAULT_KP_LOOP_ITERATIONS = 5000
DEFAULT_HOLD_METHOD = Stop.BRAKE
DEFAULT_WAIT_TIME = 750


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
