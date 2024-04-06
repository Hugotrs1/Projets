const int inputVoltage = 95; // N
const int nominalVoltage = 5; // V
const int MAX_SPEED = 150;
const int directionA = 12;
const int directionB = 13;
const int brakeA = 59;
const int brakeB = 10; // Remplacez 10 par le numéro de broche que vous utilisez.
const int speedA = 3;
const int speedB = 11;
const int in2 = A2;
const int in3 = A3;

void setup() {
  // Initialisation de la broche
  pinMode(directionA, OUTPUT);
  pinMode(brakeA, OUTPUT);
  pinMode(directionB, OUTPUT);
  pinMode(brakeB, OUTPUT);
  Serial.begin(9600);
  Serial.println(F("Initialize System"));
}

void loop() {
  readSensorM5();
  testMotorM5();
  //testStepperM5();
}

void testStepperM5() {
  // Test stepper
  Serial.println(F("Move stepper 1 step clockwise"));
  stpCW(1);
  Serial.println(F("Move stepper 1 step counter clockwise"));
  stpCCW(1);
}

void testMotorM5() {
  // Test DC motor
  Serial.println(F("Avant"));
  dcForward();
  delay(500);
  Serial.println(F("Arrière"));
  dcBackward();
  delay(500);
  Serial.println(F("Arrêt"));
  dcStop();
  delay(1000);
}

void readSensorM5() {
  // Read sensors
  Serial.print(F("In2 : "));
  Serial.println(analogRead(in2));
  Serial.print(F("In3 : "));
  Serial.println(analogRead(in3));
}

void dcForward() {
  // Set forward motion for A and B
  digitalWrite(directionA, HIGH);
  digitalWrite(brakeA, LOW);
  analogWrite(speedA, MAX_SPEED);
  digitalWrite(directionB, HIGH);
  digitalWrite(brakeB, LOW);
  analogWrite(speedB, MAX_SPEED);
}

void dcBackward() {
  // Set backward motion for A and B
  digitalWrite(directionA, LOW);
  digitalWrite(brakeA, LOW);
  analogWrite(speedA, MAX_SPEED);
  digitalWrite(directionB, LOW);
  digitalWrite(brakeB, LOW);
  analogWrite(speedB, MAX_SPEED);
}

void dcStop() {
  // Stop motors A and B
  digitalWrite(brakeA, HIGH);
  analogWrite(speedA, 0);
  digitalWrite(brakeB, HIGH);
  analogWrite(speedB, 0);
}

void stpCW(int nbStep) {
  // Move stepper clockwise
  for (int i = 0; i < nbStep; i++) {
    digitalWrite(brakeA, LOW);
    digitalWrite(brakeB, HIGH);
    digitalWrite(directionA, HIGH);
    analogWrite(speedA, MAX_SPEED);
    delay(30);
    digitalWrite(brakeA, HIGH);
    digitalWrite(brakeB, LOW);
    digitalWrite(directionB, LOW);
    analogWrite(speedB, MAX_SPEED);
    delay(30);
    digitalWrite(brakeA, LOW);
    digitalWrite(brakeB, HIGH);
    digitalWrite(directionA, LOW);
    analogWrite(speedA, MAX_SPEED);
    delay(30);
    digitalWrite(brakeA, HIGH);
    digitalWrite(brakeB, LOW);
    digitalWrite(directionB, HIGH);
    analogWrite(speedB, MAX_SPEED);
    delay(30);
  }
}

void stpCCW(int nbStep) {
  // Move stepper counter clockwise
  for (int i = 0; i < nbStep; i++) {
    digitalWrite(brakeA, LOW);
    digitalWrite(brakeB, HIGH);
    digitalWrite(directionA, LOW);
    analogWrite(speedA, MAX_SPEED);
    delay(30);
    digitalWrite(brakeA, HIGH);
    digitalWrite(brakeB, LOW);
    digitalWrite(directionB, HIGH);
    analogWrite(speedB, MAX_SPEED);
    delay(30);
    digitalWrite(brakeA, LOW);
    digitalWrite(brakeB, HIGH);
    digitalWrite(directionA, HIGH);
    analogWrite(speedA, MAX_SPEED);
    delay(30);
    digitalWrite(brakeA, HIGH);
    digitalWrite(brakeB, LOW);
    digitalWrite(directionB, LOW);
    analogWrite(speedB, MAX_SPEED);
    delay(30);
  }
}
