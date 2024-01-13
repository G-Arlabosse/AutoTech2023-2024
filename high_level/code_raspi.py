import serial
import time 
import struct 


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)   #à changer avec le bon port arduino
    ser.reset_input_buffer()

    def sendOrder(ordre : int, argument : int): #octet1 and octet2 should not be more that 8 bits
        trame = struct.pack("<BB", ordre, argument) 
        ser.write(trame)

    while True:
        tmp = input("ordre puis argument : ")
        ordre, argument = map(int, tmp.split())
        sendOrder(ordre, argument)
        #print(ser.readline())
        #time.sleep(3)
    ser.close()


    

