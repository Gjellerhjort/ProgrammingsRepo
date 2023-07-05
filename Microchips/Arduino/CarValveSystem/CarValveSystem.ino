int state = 0;
#include <Wire.h>

void setup() {
  Serial.begin(9600); // Default communication rate of the Bluetooth module
}

void loop() {
  if(Serial.available() > 0){ // Checks whether data is comming from the serial port
    state = Serial.read(); // Reads the data from the serial port
    Wire.beginTransmission(9); // transmit to device #9
    Wire.write(state); // sends x 
    Wire.endTransmission();    // stop transmitting
    delay(500);
 }

 if (state == '0') {
  Serial.println("EHY"); // Send back, to the phone, the String "LED: ON"
  state = 0;
 }
 else if (state == '1') {
  Serial.println("EH");;
  state = 0;
 }
}