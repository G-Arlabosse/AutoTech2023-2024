import serial
import time 
from car import Car
import pygame
import os
# from pynput.keyboard import Key, Listener

"""
def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.up:
        move("UP")
    if key == Key.down:
        move("DOWN")
    if key == Key.right:
        move("RIGHT")
    if key == Key.left:
        move("LEFT")
    if key == Key.up:
        move("UP")
        return False

def move(instruction):
    if instruction == "RIGHT":
        car.turn_right()
    if instruction == "LEFT":
        car.turn_left()
    if instruction == "UP":
        car.speed_up()
    if instruction == "DOWN":
        car.speed_down()
    if instruction == "QUIT":
        done = True
        car.stop()

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
"""
if __name__ == '__main__':

    os.environ["SDL_VIDEODRIVER"] = "dummy" #Fix pour avoir un faux driver vidéo pour que Pygame fonctionne

    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)   #à changer avec le bon port arduino
    ser.reset_input_buffer()
    car = Car(ser)

    pygame.init()
    size = (800, 600)  # Width, Height
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My Pygame Window")
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

    """
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('You Pressed A Key!')
                break  # finishing the loop
        except:
            break  # if user pressed a key other than the given key the loop will break
    """

pygame.quit()
ser.close()


