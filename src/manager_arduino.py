import serial
import time 
from car import Car
import pygame
import os

if __name__ == '__main__':

    os.environ["SDL_VIDEODRIVER"] = "dummy" #Fix pour avoir un faux driver vidéo pour que Pygame fonctionne

    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)   #à changer avec le bon port arduino
    ser.reset_input_buffer()

    pygame.init()
    size = (800, 600)  # Width, Height
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My Pygame Window")
    car = Car(ser)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    car.turn_right()
                if event.key == pygame.K_LEFT:
                    car.turn_left()
                if event.key == pygame.K_UP:
                    car.speed_up()
                if event.key == pygame.K_DOWN:
                    car.speed_down()
                if event.key == pygame.K_q:
                    done = True
                    car.stop()


pygame.quit()
ser.close()


