volatile byte rpmcount = 0;
unsigned long rpm = 0;
int interruptPin = 3;
int lift = 60; // dette er i ms
int duration = 100; // dette er i ms

void setup() {
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(interruptPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(interruptPin),rpmtrigger,FALLING);
}



void loop() {
  digitalWrite(5, HIGH);
  digitalWrite(6, HIGH);
  delay(lift+ );
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  delay(lift);
}

void rpmtrigger()
{
 rpmcount++;
}