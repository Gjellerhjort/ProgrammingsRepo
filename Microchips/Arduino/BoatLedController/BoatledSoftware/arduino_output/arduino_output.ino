
// Include the required Wire library for I2C<br>#include <Wire.h>
#include <Wire.h>
#include "Tlc5940.h"

// === Remote setup ===
struct REMOTE{
  uint16_t bright;   uint16_t dim;        uint16_t pause;     uint16_t power;
  uint16_t red1;     uint16_t green1;     uint16_t blue1;     uint16_t white1; 
  uint16_t red2;     uint16_t green2;     uint16_t blue2;     uint16_t white2; 
  uint16_t red3;     uint16_t green3;     uint16_t blue3;     uint16_t white3; 
  uint16_t red4;     uint16_t green4;     uint16_t blue4;     uint16_t white4; 
  uint16_t red5;     uint16_t green5;     uint16_t blue5;     uint16_t white5; 
  uint16_t red_up;   uint16_t green_up;   uint16_t blue_up;   uint16_t quick; 
  uint16_t red_down; uint16_t green_down; uint16_t blue_down; uint16_t slow; 
  uint16_t diy1;     uint16_t diy2;       uint16_t diy3;      uint16_t autom; 
  uint16_t diy4;     uint16_t diy5;       uint16_t diy6;      uint16_t flash; 
  uint16_t jump3;    uint16_t jump7;      uint16_t fade3;     uint16_t fade7;
};

// These are the codes for my remote. Use IRLremote Receive example to decode your remote.
const REMOTE remote = {
  0x5C,0x5D,0x41,0x40,
  0x58,0x59,0x45,0x44,
  0x54,0x55,0x49,0x48,
  0x50,0x51,0x4D,0x4C,
  0x1C,0x1D,0x1E,0x1F,
  0x18,0x19,0x1A,0x1B,
  0x14,0x15,0x16,0x17,
  0x10,0x11,0x12,0x13,
  0x0C,0x0D,0x0E,0x0F,
  0x08,0x09,0x0A,0x0B,
  0x04,0x05,0x06,0x07
};

int LED = 6;
volatile int message = 0;
volatile int lastmessage = 0;
double brightness = 1;

unsigned long previousMillis = 0;
unsigned long interval = 1000;  // Delay interval in milliseconds


void setStrip(int strip, int r, int g, int b) {
  int baseIndex = strip * 3;
  Tlc.set(baseIndex, map(r * brightness, 0, 255, 4095, 0));
  Tlc.set(baseIndex + 1, map(g * brightness, 0, 255, 4095, 0));
  Tlc.set(baseIndex + 2, map(b * brightness, 0, 255, 4095, 0));
  Tlc.update();
  delay(5);
}

void setStripAll(int r, int g, int b) {
  setStrip(0, r, g, b);
  setStrip(1, r, g, b);
  setStrip(2, r, g, b);
  setStrip(3, r, g, b);
  setStrip(4, r, g, b);
}

void receiveEvent(int bytes) {
    while (Wire.available()) {
    // Read the received data from the I2C bus
    message = Wire.read();    // read one character from the I2C
  }
}

void setup() {
  Serial.begin(9600);
  // Define the LED pin as Output
  pinMode(6, OUTPUT);
  Tlc.init(0);

  // Start the I2C Bus as Slave on address 9
  Wire.begin(9); 
  // Attach a function to trigger when something is received.
  Wire.onReceive(receiveEvent);
}
 
void loop() {
  if (message == 0x00) {
    message = lastmessage;
  }

  if (message != lastmessage) {
    if (message == remote.dim) {
      setStripAll(0, 0, 0);
    } 
    else if (message == remote.red1) {
      setStripAll(255, 0, 0);
    } 
    else if (message == remote.green1) {
      setStripAll(0, 255, 0);
    } 
    else if (message == remote.blue1) {
      setStripAll(0, 0, 255);
    } 
    else if (message == remote.white1) {
      setStripAll(255, 255, 255);
    }
    lastmessage = message;
  }

  if (message == remote.diy1) {
    static int state = 0;
    unsigned long currentMillis = millis();
    
    if (currentMillis - previousMillis >= interval) {
      previousMillis = currentMillis;
      
      if (state == 0) {
        setStrip(0, 0, 0, 255);
        setStrip(1, 0, 0, 255);
        setStrip(2, 255, 0, 0);
        setStrip(3, 255, 0, 0);
      } else if (state == 1) {
        setStrip(0, 255, 0, 0);
        setStrip(1, 255, 0, 0);
        setStrip(2, 0, 0, 255);
        setStrip(3, 0, 0, 255);
      }
      
      state = 1 - state;
    }
  } 
  else if (message == remote.diy2) {
    static int state = 0;
    unsigned long currentMillis = millis();
    
    if (currentMillis - previousMillis >= interval) {
      previousMillis = currentMillis;
      
      if (state == 0) {
        setStrip(0, 255, 0, 0);
        setStrip(1, 255, 255, 255);
        setStrip(2, 255, 255, 255);
        setStrip(3, 255, 255, 255);
      } else if (state == 1) {
        setStrip(0, 255, 255, 255);
        setStrip(1, 255, 0, 0);
        setStrip(2, 255, 255, 255);
        setStrip(3, 255, 255, 255);
      } else if (state == 2) {
        setStrip(0, 255, 255, 255);
        setStrip(1, 255, 255, 255);
        setStrip(2, 255, 0, 0);
        setStrip(3, 255, 255, 255);
      } else if (state == 3) {
        setStrip(0, 255, 255, 255);
        setStrip(1, 255, 255, 255);
        setStrip(2, 255, 255, 255);
        setStrip(3, 255, 0, 0);
      }
      
      state = (state + 1) % 4;
    }
  }  
  else if (message == remote.diy3) {
    static int state = 0;
    unsigned long currentMillis = millis();
    
    if (currentMillis - previousMillis >= interval) {
      previousMillis = currentMillis;
      
      if (state == 0) {
        setStripAll(255, 0, 0);
      } else if (state == 1) {
        setStripAll(0, 255, 0);
      } else if (state == 2) {
        setStripAll(0, 0, 255);
      }
      
      state = (state + 1) % 3;
    }
  }  
  else if (message == remote.flash) {
    static int state = 0;
    unsigned long currentMillis = millis();
    
    if (currentMillis - previousMillis >= 100) {
      previousMillis = currentMillis;
      
      if (state == 0) {
        setStripAll(255, 255, 255);
      } else if (state == 1) {
        setStripAll(0, 0, 0);
      }
      
      state = 1 - state;
    }
  }
}
