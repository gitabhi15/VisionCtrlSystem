#include <Servo.h>
#include <LiquidCrystal.h>

Servo lockservo

LiquidCrystal lcd(12,11,5,4,3,2)

int state = 0

void setup(){
  Serial.begin(9600)
  lockservo.attach(9) 
  lcd.begin(16,2)
  lcd.print("system ready")
  lockservo.write(0) // locked
}

void loop(){
  if(Serial.available()>0){
    char c = Serial.read()
    if(c == '1'){
      lcd.clear()
      lcd.print("access granted")
      lockservo.write(90) // open
      delay(5000)
      lockservo.write(0)
      lcd.clear()
      lcd.print("locked")
    }
    if(c == '0'){
      lcd.clear()
      lcd.print("access denied")
      lockservo.write(0)
    }
  }
}
