#include <SoftwareSerial.h>
#define BT_TX 12
#define BT_RX 13

// 핀 설정
int A_1 = 10, A_2 = 11, B_1 = 5, B_2 = 9;
int Line_R = 7, Line_L = 6, trigPin = 4, echoPin = 3;

SoftwareSerial BTSerial(BT_TX, BT_RX);

// 모터 동작을 위한 함수
void controlMotors(int L1, int L2, int R1, int R2) {
  analogWrite(A_1, L1);
  analogWrite(A_2, L2);
  analogWrite(B_1, R1);
  analogWrite(B_2, R2);
}

// 초음파 센서를 이용한 거리 측정 함수(cm)
long readUltrasonicDistance() {
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

void setup() {  
  Serial.begin(9600);
  BTSerial.begin(9600);
  pinMode(A_1, OUTPUT); pinMode(A_2, OUTPUT);
  pinMode(B_1, OUTPUT); pinMode(B_2, OUTPUT);
  pinMode(Line_R, INPUT); pinMode(Line_L, INPUT);
  pinMode(trigPin, OUTPUT); pinMode(echoPin, INPUT);

  controlMotors(0, 0, 0, 0); // 모터 초기화
}

void loop() {
  if (BTSerial.available()) {
    char cmd = BTSerial.read();
    Serial.print(cmd);

    long distance = readUltrasonicDistance(); // 초음파 센서로 거리 측정

    // 물체가 감지되었을 때 후진을 제외한 모든 동작은 정지
    if (distance >= 0.01 && distance <= 15 && cmd != 'B') {
      controlMotors(0, 0, 0, 0);
      Serial.println("Obstacle detected, stopping motors");
      return; // 후진이 아닌 경우는 동작하지 않음
    }

    // 명령에 따라 동작 수행
    switch (cmd) {
      case 'D': // 전진
      controlMotors(255, 0, 248, 0);
      while(true) {
        long new_distance = readUltrasonicDistance();
        if (new_distance >= 0.01 && new_distance <= 20) {
          controlMotors(0, 0, 0, 0);
          Serial.println("Obstacle detected, stopping motors");
          break;
        }
        if (BTSerial.available() && BTSerial.read() == 'S') {
          controlMotors(0, 0, 0, 0);  // 정지 명령이 들어오면 멈춤
          break;
        }
      }
      break;
      case 'B': controlMotors(0, 255, 0, 240); break;  // 후진
      case 'R': controlMotors(200, 0, 0, 200); break;  // 우회전
      case 'L': controlMotors(0, 200, 200, 0); break;  // 좌회전
      case 'S': controlMotors(0, 0, 0, 0); break;      // 정지
      case 'x':  // 라인 트래킹 모드
        while (true) {
          char cmd1 = BTSerial.read();
          
          // 라인 트래킹 중에도 초음파 거리 측정
          long distanceDuringTracking = readUltrasonicDistance();
<<<<<<< HEAD
          if (distanceDuringTracking <= 15 && distanceDuringTracking >= 0.01 ) {
=======
          if (distanceDuringTracking >= 0.01 && distanceDuringTracking <= 15 && cmd1 != 'B') {
>>>>>>> 4bb627034b1c9e8cf5feb99089d660413b611a59
            controlMotors(0, 0, 0, 0);
            Serial.println("Obstacle detected during tracking, stopping motors");
            //break; // 물체가 감지되면 라인 트래킹도 중단
          }

          if (!digitalRead(Line_R) && !digitalRead(Line_L)) {
<<<<<<< HEAD
            controlMotors(205, 0, 200, 0); // 직진
=======
            controlMotors(118, 0, 115, 0); // 직진
>>>>>>> 4bb627034b1c9e8cf5feb99089d660413b611a59
          } 
          else if (digitalRead(Line_R) && !digitalRead(Line_L)) {
            controlMotors(0, 0, 0, 150); // 오른쪽 회피
            delay(300); //밀리초
          } 
          else if (!digitalRead(Line_R) && digitalRead(Line_L)) {
            controlMotors(0, 150, 0, 0); // 왼쪽 회피
            delay(300); //밀리초
          } 
          else {
            controlMotors(0, 0, 0, 0); // 정지
          }
          if (cmd1 == 'y') { // 라인 트래킹 종료
            controlMotors(0, 0, 0, 0);
            break;
          }
        }
        break;
    }
  }
}
