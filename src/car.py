import struct 
import time

ANGLE_DIFFERENTIAL = 10
SPEED_ARGUMENT_MAX = 170
SPEED_ARGUMENT_MIN = 100




class Car:
    def __init__(self, serial):
        self.serial = serial
        self.speed_argument = 150
        self.angle_argument = 137
    
    def sendOrder(self, ordre : int, argument : int): #octet1 and octet2 should not be more that 8 bits
        trame = struct.pack("<BB", ordre, argument) 
        self.serial.write(trame)

    def turn_right(self):
        ordre = 97
        self.angle_argument = min(155, self.angle_argument+10)
        self.sendOrder(ordre, self.angle_argument)

    def turn_left(self):
        ordre = 97
        self.angle_argument = max(118, self.angle_argument-10)
        self.sendOrder(ordre, self.angle_argument)

    def speed_up(self):
        ordre = 98
        self.speed_argument = min(SPEED_ARGUMENT_MAX, self.speed_argument+1)
        self.sendOrder(ordre, self.speed_argument)

    def speed_down(self):
        ordre = 98
        self.speed_argument = max(SPEED_ARGUMENT_MIN, self.speed_argument-1)
        self.sendOrder(ordre, self.speed_argument)

    def reset(self):
        self.speed_argument = 150
        self.angle_argument = 137
        self.sendOrder(97, self.angle_argument)
        self.sendOrder(98, self.angle_argument)

    def stop(self):
        self.sendOrder(98, SPEED_ARGUMENT_MIN)
        time.sleep(1)
        self.reset()