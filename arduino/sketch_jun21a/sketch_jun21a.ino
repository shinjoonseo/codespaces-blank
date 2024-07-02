int trigPin = 4;
int echoPin = 3;

void setup(){
  Serial.begin(9600);
  pinMode(echoPin, INPUT);
  pinMode(trigPin, OUTPUT);
}

void loop(){
  long duration, distance;
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

// duration은 echo핀이 HIGH를 유지한 시간
  duration = pulseIn(echoPin, HIGH);

// distance = speed * time = 음속(340m/s) * duration
// 왕복 거리이므로 2로 나누기!
  distance = ((float)(340*duration)/1000)/2;

  Serial.print("\nDistance:");
  Serial.print(distance);
  Serial.println("mm\n");
}
