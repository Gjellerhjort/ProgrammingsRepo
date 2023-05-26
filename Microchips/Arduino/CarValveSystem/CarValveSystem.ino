volatile byte rpmcount = 0;
unsigned long rpm = 0;
int interruptPin = 3;
int lift = 30; // dette er i ms
int duration = 15; // dette er i ms
int BUTTON_PIN = 2;

void setup() {
  Serial.begin(9600);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(2, INPUT);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  attachInterrupt(2, RpmMode, FALLING); 
}



void loop() {

  lift = analogRead(A0);
  duration = analogRead(A1);
  duration = map(duration, 0, 1023,30, 400);
  lift = map(lift, 0, 1023,30, 400);
  Serial.println(lift);
  Serial.println(rpm);
  digitalWrite(5, HIGH);
  digitalWrite(6, HIGH);
  delay(duration);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  delay(lift);
}

void rpmtrigger()
{
 rpmcount++;
}

void RpmMode() {
  rpm = rpm + 1000;
  if (rpm > 10000)
  
{
  rpm=0;      
}  
}