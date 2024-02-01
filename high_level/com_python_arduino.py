import serial
import time 
import struct 



if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)   #à changer avec le bon port arduino
    ser.reset_input_buffer()

    def sendOrder(ordre : int, argument : float): #octet1 and octet2 should not be more that 8 bits
        trame = struct.pack("<Bf", ordre, argument) 
        ser.write(trame)

    while True:
        tmp = input("ordre puis argument : ")
        args = tmp.split()
        ordre, argument = int(args[0]), float(args[1])
        sendOrder(ordre, argument)
        #print(ser.readline())
        #time.sleep(3)
    ser.close()


    

