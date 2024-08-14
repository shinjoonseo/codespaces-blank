#include <SoftwareSerial.h>
#define BT_TX 12
#define BT_RX 13

int A_1 = 10;
int A_2 = 11;
int B_1 = 5;
int B_2 = 9;
int Line_R = 7;
int Line_L = 6;
int trigPin = 4;
int echoPin = 3;

SoftwareSerial BTSerial(BT_TX,BT_RX);

void setup() {  
  Serial.begin(9600);
  BTSerial.begin(9600);
  pinMode(A_1, OUTPUT);
  pinMode(A_2, OUTPUT);
  pinMode(B_1, OUTPUT);
  pinMode(B_2, OUTPUT);
  digitalWrite(A_1, LOW);
  digitalWrite(A_2, LOW);
  digitalWrite(B_1, LOW);
  digitalWrite(B_2, LOW);

  pinMode(Line_R, INPUT);
  pinMode(Line_L, INPUT);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}
void loop() {
  char cmd ;
  if (BTSerial.available()) {
    cmd = BTSerial.read();
    Serial.print(cmd);

    switch (cmd) {
      case 'D' :
        analogWrite(A_1, 255);
        analogWrite(A_2, 0);
        analogWrite(B_1, 255);
        analogWrite(B_2, 0);
        break;
      case 'B' :
        analogWrite(A_1, 0);
        analogWrite(A_2, 255);
        analogWrite(B_1, 0);
        analogWrite(B_2, 255);
        break;
      case 'R' :
        analogWrite(A_1, 200);
        analogWrite(A_2, 0);
        analogWrite(B_1, 0);
        analogWrite(B_2, 200);
        break;
      case 'L' :
        analogWrite(A_1, 0);
        analogWrite(A_2, 200);
        analogWrite(B_1, 200);
        analogWrite(B_2, 0);
        break;
      case 'S' :
        analogWrite(A_1, 0);
        analogWrite(A_2, 0);
        analogWrite(B_1, 0);
        analogWrite(B_2, 0);
        break;
    }

    while (cmd == 'x') {
      char cmd1 = BTSerial.read();
      if (!digitalRead(Line_R) && !digitalRead(Line_L)) {
        analogWrite(A_1, 100);
        analogWrite(A_2, 0);
        analogWrite(B_1, 100);
        analogWrite(B_2, 0);
      }
      else if (digitalRead(Line_R) && !digitalRead(Line_L)) {
        analogWrite(A_1, 100);
        analogWrite(A_2, 0);
        analogWrite(B_1, 0);
        analogWrite(B_2, 200);
      }
      else if (!digitalRead(Line_R) && digitalRead(Line_L)) {
        analogWrite(A_1, 0);
        analogWrite(A_2, 200);
        analogWrite(B_1, 100);
        analogWrite(B_2, 0);
      } 
      else if (digitalRead(Line_R) && digitalRead(Line_L)) {
        analogWrite(A_1, 0);
        analogWrite(A_2, 0);
        analogWrite(B_1, 0);
        analogWrite(B_2, 0);
      }
      if (cmd1 == 'y') {
        analogWrite(A_1, 0);
        analogWrite(A_2, 0);
        analogWrite(B_1, 0);
        analogWrite(B_2, 0);
        break ;
      }
    }
  }
}
