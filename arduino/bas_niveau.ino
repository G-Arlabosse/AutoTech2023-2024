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
  
  angle.attach(PINangle, 1180, 1550);         //largeur impulsion positive 5V
  esc.attach(PINspeed, 0, 2000);

  esc.writeMicroseconds(1500);
  angle.writeMicroseconds(1370);
 
}

void loop() {
  if (Serial.available() >= 2) {
    // On lit la commande et l'argument sur le port série
    uint8_t ordre = Serial.read();
    uint8_t val = Serial.read(); //ici j'ai changé j'ai plus un octet mais un double
    //je dois modifier la ligne au-dessus pour la concordance des types
    // On effectue la commande associé
    if (ordre == AngleOrder) {
      double pwm_angle = (double)val*185+1365; //on donne entre -1 et 1 sur python: -1 tourne au max à gauche et 1 à droite
      //vérifier si les concordances des types est correcte
      Serial.print("angle: ");
      Serial.println(pwm_angle);
      // On écrit la valeur sur le servo
      angle.writeMicroseconds(pwm_angle);
    } else if (ordre == SpeedOrder) {
      double pwm_vitesse = (double)val*200+1500;  //on donne entre -1 et 1, à partir de 0 çca avance, pas de marche arrière pour l'instant
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
