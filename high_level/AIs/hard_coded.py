"""
Author(s) : 
This script represents a hard coded AI for the car
"""

# In this code, I copy the way that the example of the simulator functions

# Le code utilise des bibliothèques que je n'ai pas pu trouver...
# Les noms des fonctions étant assez clairs, on pourra faire notre propre version de ces bibliothèques
from vehicle import Driver
from controller import Lidar

class Car:

    def __init__(self, speed=0, angle=0):
        self.speed = speed
        self.angle = angle
        self.maxSpeed = 28
        self.maxAngle = 0.28
        self.driver = Driver()
        self.compteurRecul = 0

    def choixTrajectoire(self,lidar):
        front = lidar[0]
        left = lidar[315]
        right = lidar[45]
        
        if self.compteurRecul > 0:
            self.compteurRecul -= 1
            speed = -3
            angle = left - right
        else:
            speed = 3 #km/h
            #l'angle de la direction est la différence entre les mesures des rayons 
            #du lidar à (-99+18*2)=-63° et (-99+81*2)=63°
            angle = right - left
            if front > 3:
                speed = 6
            if front < min(left,right,1):
                print("hey")
                self.compteurRecul = 25
    
        return speed, angle

    def modifTrajectoire(self):
        self.driver.setCruisingSpeed(self.speed)
        self.driver.setSteeringAngle(self.angle)

    def setValues(self, spd, ang):
        if spd > self.maxSpeed:
            self.speed = self.maxSpeed
        elif spd < -1 * self.maxSpeed:
            self.speed = -1 * self.maxSpeed
        else:
            self.speed = spd
        if ang > self.maxAngle:
            self.angle = self.maxAngle
        elif ang < -self.maxAngle:
            self.angle = -self.maxAngle
        else:
            self.angle = ang


def manual(key, car):
    if key == keyboard.UP:
        car.speed += 0.2
    elif key == keyboard.DOWN:
        car.speed -= 0.2
    elif key == keyboard.LEFT:
        car.angle -= 0.04
    elif key == keyboard.RIGHT:
        car.angle += 0.04


car = Car()

basicTimeStep = int(car.driver.getBasicTimeStep())
sensorTimeStep = 4 * basicTimeStep

#Lidar
lidar = Lidar("RpLidarA2")
lidar.enable(sensorTimeStep)
lidar.enablePointCloud() 

#clavier
keyboard = car.driver.getKeyboard()
keyboard.enable(sensorTimeStep)

car.modifTrajectoire()

# mode manuel et mode auto desactive
modeManuel = False
modeAuto = False
print("cliquer sur la vue 3D pour commencer")
print("m pour mode manuel, a pour mode auto, n pour stop, l pour affichage données lidar")
print("en mode manuel utiliser les flèches pour accélérer, freiner et diriger")

while car.driver.step() != -1:

    speed = car.driver.getTargetCruisingSpeed()

    while True:
        #acquisition des donnees du lidar
        donnees_lidar = lidar.getRangeImage()
        
        # recuperation de la touche clavier
        currentKey = keyboard.getKey()
        if currentKey == -1:
            break
        if currentKey == ord('m') or currentKey == ord('M'):
            if not modeManuel:
                modeManuel = True
                modeAuto = False
                print("------------Mode Manuel Activé---------------")
        elif currentKey == ord('n') or currentKey == ord('N'):
            if modeManuel or modeAuto :
                modeManuel = False
                modeAuto = False
                print("--------Modes Manuel et Auto Désactivé-------")
        elif currentKey == ord('a') or currentKey == ord('A'):
            if not modeAuto : 
                modeAuto = True
                modeManuel = False
                print("------------Mode Auto Activé-----------------")
        elif currentKey == ord('l') or currentKey == ord('L'):
                print("-----donnees du lidar en metres sens horaire au pas de 1°-----")
                for i in range(len(donnees_lidar)) :
                    print(f"{donnees_lidar[i]:.3f}   ", end='')
                    if (i+1)%10 == 0 :        
                       print()
                print()
      
        # Controle en mode manuel
        if modeManuel:
            manual(currentKey, car)
            

    if not modeManuel and not modeAuto:
        speed = 0
        angle = 0
        
    if modeAuto:

        speed, angle = car.choixTrajectoire(donnees_lidar)

    # clamp speed and angle to max values
    car.setValues(speed,angle)

    car.modifTrajectoire()
