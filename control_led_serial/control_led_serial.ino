#include <Arduino.h>

const int ledPin = 13;

void setup(){
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  if (Serial.available()) {
    light(Serial.read() - '0');
  }
  delay(500);
}


//Funcion que parpadea el led n veces siendo n : n<10 && n>0
void light(int n){
  for (int i = 0; i < n; i++) {
    digitalWrite(ledPin, HIGH);
    delay(500);
    digitalWrite(ledPin, LOW);
    delay(500);
  }
}
