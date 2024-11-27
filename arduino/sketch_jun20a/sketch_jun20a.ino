// 변수세팅

#include <SoftwareSerial.h>

#define bttx 12
#define btrx 13

int l1 = 10; // 왼쪽바퀴(+)
int l2 = 11; // 왼쪽바퀴(-)
int r1 = 5; // 오른쪽바퀴(+)
int r2 = 9; // 오른쪽바퀴(-)

int liner = 7; // 오른쪽 센서
int linel = 6; // 왼쪽 센서

// 초음파 센서
int trigPin = 4; // 내보냄
int echoPin = 3; // 받아들여서 감지함 

SoftwareSerial BtSerial(bttx, btrx);

void setup(){ 
  Serial.begin(9600); // 시리얼통신 속도 선언
  BtSerial.begin(9600); // 초기화 선언
  pinMode(trigPin, OUTPUT); // 포트에 전기를(무언가를 ex. 에너지) 내보내기만함(모터를 작동하기 위해서)
  pinMode(l1, OUTPUT);
  pinMode(l2, OUTPUT);
  pinMode(r1, OUTPUT);
  pinMode(r2, OUTPUT); 

  pinMode(echoPin, INPUT); // 동작하기 위해 특정 값을 받아들임(ex. 앞에 물건이 있으면 물건을 인식함)
  pinMode(liner, INPUT);
  pinMode(linel, INPUT);

  digitalWrite(l1, LOW); 
  digitalWrite(l2, LOW);
  digitalWrite(r1, LOW);
  digitalWrite(r2, LOW);
}

long readUltrasonicDistance() { // 초음파 센서 거리 측정
  long timeout = 100 * 1000L / 34 * 2;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH, timeout);
  long distance = (duration * 0.0343) / 2; // 거리(cm) 계산
  return distance;
}

void loop(){
  char cmd;
  long distance = readUltrasonicDistance();

  if (BtSerial.available()) {
    cmd = BtSerial.read();
    Serial.print(cmd); // 확인용

    if (distance < 15 && distance > 0.1 && cmd != 'S'){
      analogWrite(l1, 0);
      analogWrite(r1, 0);
      analogWrite(l2, 0);
      analogWrite(r2, 0);
      return;
    } 
    if (cmd == 'D'){
      analogWrite(l1, 255);
      analogWrite(r1, 255);
      analogWrite(l2, 0);
      analogWrite(r2, 0);

      while (true) {
        long newdistance = readUltrasonicDistance();
        if (newdistance < 15 && newdistance > 0.1){
          analogWrite(l1, 0);
          analogWrite(r1, 0);
          analogWrite(l2, 0);
          analogWrite(r2, 0);
          break;
        }
        if (BtSerial.available() && BtSerial.read() == 'S'){
          analogWrite(l1, 0);
          analogWrite(r1, 0);
          analogWrite(l2, 0);
          analogWrite(r2, 0);
          break;
        }
      }
    }
    else if (cmd == 'L'){
      analogWrite(r1, 200);
      analogWrite(l1, 0);
      analogWrite(r2, 0);
      analogWrite(l2, 200);
    }
    else if (cmd == 'B'){
      analogWrite(l2, 255);
      analogWrite(r2, 255);
      analogWrite(l1, 0);
      analogWrite(r1, 0);
    }
    else if (cmd == 'R'){
      analogWrite(l1, 200);
      analogWrite(l2, 0);
      analogWrite(r1, 0);
      analogWrite(r2, 200);
    }
    else if (cmd == 'S'){
      analogWrite(r1, 0);
      analogWrite(r2, 0);
      analogWrite(l1, 0);
      analogWrite(l2, 0);
    }
    else if (cmd == 'x'){ // 라인모드 ON
      linemode();
    }
  }
}

void linemode() {
  char cmd;
  while (true) {
    cmd = BtSerial.read();
    long newdistance = readUltrasonicDistance();
    if (newdistance < 15 && newdistance > 0.1){
      analogWrite(l1, 0);
      analogWrite(r1, 0);
      analogWrite(l2, 0);
      analogWrite(r2, 0);
      break;
    }


    if (cmd == 'y'){ // 라인모드 OFF
      analogWrite(r1, 0);
      analogWrite(r2, 0);
      analogWrite(l1, 0);
      analogWrite(l2, 0);
      break;
    }
    if (digitalRead(linel) && !digitalRead(liner)){ // 오른쪽 
      analogWrite(r1, 100);
      analogWrite(l1, 0);
      analogWrite(r2, 0);
      analogWrite(l2, 0);
    }
    else if (!digitalRead(linel) && digitalRead(liner)){
      analogWrite(l1, 100);
      analogWrite(l2, 0);
      analogWrite(r1, 0);
      analogWrite(r2, 0);
    }
    else if (!digitalRead(linel) && !digitalRead(liner)){ // 왼쪽, 오른쪽 센서에 라인 감지가 안 될 때
      analogWrite(l1, 120);
      analogWrite(r1, 120);
      analogWrite(l2, 0);
      analogWrite(r2, 0);
    }
    else if (digitalRead(linel) && digitalRead(liner)){ // 정지선
      analogWrite(l1, 0);
      analogWrite(r1, 0);
      analogWrite(l2, 0);
      analogWrite(r2, 0);
    }
  }
}
