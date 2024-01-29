#include <Servo.h>

#define AngleOrder 97
#define SpeedOrder 98
#define changeMoovOrder 99
#define changeRotaOrder 100

#define PINangle  11
#define PINspeed  10


Servo angle;
Servo esc;

//------------------------------------------
void setup() {
  Serial.begin(115200);
  
  pinMode(PINangle, OUTPUT);
  pinMode(PINspeed, OUTPUT);
  
  angle.attach(PINangle, 1000, 2000);         //largeur impulsion positive 5V
  esc.attach(PINspeed, 1000, 2000);

  esc.writeMicroseconds(1500);
  angle.writeMicroseconds(1300);
 
}

void loop() {
  if (Serial.available() >= 2) {
    // On lit la commande et l'argument sur le port série
    uint8_t ordre = Serial.read();
    uint8_t val = Serial.read();

    // On effectue la commande associé
    if (ordre == AngleOrder) {
      int pwm_angle = (int)val*10;
      
      Serial.print("angle: ");
      Serial.println(pwm_angle);
      // On écrit la valeur sur le servo
      angle.writeMicroseconds(pwm_angle);
    } else if (ordre == SpeedOrder) {
      
      int pwm_vitesse = (int)val*10;
      Serial.print("speed: ");
      Serial.println(pwm_vitesse);
      // On écrit sur l'ESC
      esc.writeMicroseconds(pwm_vitesse); 
    }
    /*
    // arg == 0 => dir = -1 | arg == 1 => dir = 1
    else if (order == changeMoovOrder){
     dirSpeed = -1 + 2 * arg;  
    }
    else if (order == changeRotaOrder) {
     dirAngle = -1 + 2 * arg;
    }*/
  }
  
}