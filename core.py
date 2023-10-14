from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase

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