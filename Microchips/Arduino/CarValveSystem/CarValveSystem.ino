#define BUTTON_PIN 2

volatile int rpm = 0;
int prevRpm;
int mode = 0;
float valveLiftTime; // dette er i ms
float prevValveLiftTime;
float valveOffset; // dette er i ms
float valveOffTime; // dette er i ms
float prevValveOffsetTime;
float valveTiming;
float timeBetweenValveOpenings;
float prevTimeBetweenValveOpenings;
int valveOffsetPercent;
int valveLiftTimePercent;
volatile unsigned long buttonLastPressedTime = 0;
const unsigned long debounceDelay = 200;  // tryk delay


void setup() {
  Serial.begin(9600);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  attachInterrupt(digitalPinToInterrupt(BUTTON_PIN), RpmMode, FALLING); 
}



void loop() {
  valveLiftTime = analogRead(A0);
  valveOffset = analogRead(A1);
  valveOffsetPercent = map(valveOffset, 0, 1023, 0, 50);
  valveLiftTimePercent = map(valveLiftTime, 0, 1023, 0, 50);

  valveTiming = 60000.0 / rpm;
  valveOffset = valveTiming * valveOffsetPercent / 100.0;
  valveLiftTime = valveTiming * valveLiftTimePercent / 100.0;
  timeBetweenValveOpenings = valveTiming - valveOffset - valveLiftTime;

  digitalWrite(5, HIGH);
  delay(valveOffset);
  digitalWrite(6, HIGH);
  delay(valveLiftTime);
  digitalWrite(5, LOW);
  delay(valveOffset);
  digitalWrite(6, LOW);
  delay(timeBetweenValveOpenings);
  /*
  if (valveOffset != prevValveOffsetTime || valveLiftTime != prevValveLiftTime || timeBetweenValveOpenings != prevTimeBetweenValveOpenings || rpm != prevRpm)
  {
    Serial.print("Rpm: ");
    Serial.println(rpm);
    Serial.print("valveOffsetTime: ");
    Serial.println(valveOffset);
    Serial.print("valveLiftTime: ");
    Serial.println(valveLiftTime);
    Serial.print("timeBetweenValveOpenings: ");
    Serial.println(timeBetweenValveOpenings);
    
    prevRpm = rpm;
    prevValveOffsetTime = valveOffset;
    prevValveLiftTime = valveLiftTime;
    prevTimeBetweenValveOpenings = timeBetweenValveOpenings;
    
  }
  */
}


void RpmMode() {
  // får nuværne tid
  unsigned long currentMillis = millis();
  // tjekker om der er gået 200 ms siden sidste tryk så den ikke registere flere tryk
  if (currentMillis - buttonLastPressedTime >= debounceDelay) {
    // plusser 1 til mode variblen
    mode++;
    // gemmer den nuværnde tid 
    buttonLastPressedTime = currentMillis;
  }
  else
  {
    // ellers stopper koden her
    return;
  }
  // hvis mode er over eller ligmed 7 bliver mode sat til 0
  if (mode >= 7)
  {
    mode = 0;
  }
  // printer variablen mode over UART
  Serial.println(mode);
  // sætter rpm til forskellige værdier efter hvilket mode er sat
  switch (mode) {
  case 0:
    rpm = 50;
    break;
  case 1:
    rpm = 100;
  break;
  case 2:
    rpm = 200;
    break;
  case 3:
    rpm = 500;
    break;
  case 4:
    rpm = 1000;
    break;
  case 5:
    rpm = 4000;
    break;
  case 6:
    rpm = 6500;
    break;
  default:
    rpm = 0;
    break;
  }
  // printer nuværne omdrejninger
  Serial.println(rpm);
}