import struct 
import time


class Car:

    self.ANGLE_DIFFERENTIAL = 0.1
    self.SPEED_ARGUMENT_MAX = 1
    self.SPEED_ARGUMENT_MIN = 0
    self.ANGLE_ARGUMENT_MAX = 1
    self.ANGLE_ARGUMENT_MIN = -1

    
    def __init__(self, serial):
        self.serial = serial
        self.speed_argument = 0
        self.angle_argument = 0
    
    def send_commands(self, linear_cmd: float, angular_cmd: float):
        assert linear_cmd >= 0 and linear_cmd <= 1, "Linear cmd must be in [0, 1]"
        assert angular_cmd >= -1 and angular_cmd <= 1, "Angular comd must be in [-1, 1]"

        

    def sendOrder(self, ordre : int, argument : int): #octet1 and octet2 should not be more that 8 bits
        trame = struct.pack("<Bf", ordre, argument) 
        self.serial.write(trame)

    def turn_right(self):
        ordre = 97
        self.angle_argument = min(ANGLE_ARGUMENT_MAX, self.angle_argument+0.1)
        self.sendOrder(ordre, self.angle_argument)

    def turn_left(self):
        ordre = 97
        self.angle_argument = max(ANGLE_ARGUMENT_MIN, self.angle_argument-0.1)
        self.sendOrder(ordre, self.angle_argument)

    def speed_up(self):
        ordre = 98
        self.speed_argument = min(SPEED_ARGUMENT_MAX, self.speed_argument+0.1)
        self.sendOrder(ordre, self.speed_argument)

    def speed_down(self):
        ordre = 98
        self.speed_argument = max(SPEED_ARGUMENT_MIN, self.speed_argument-0.1)
        self.sendOrder(ordre, self.speed_argument)

    def reset(self):
        self.speed_argument = 0
        self.angle_argument = 0
        self.sendOrder(97, self.angle_argument)
        self.sendOrder(98, self.angle_argument)

    def stop(self):
        self.sendOrder(98, SPEED_ARGUMENT_MIN)
        time.sleep(1)
        self.reset()