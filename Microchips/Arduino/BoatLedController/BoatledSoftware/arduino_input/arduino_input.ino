#include <Wire.h>
#include <SoftwareSerial.h>

int lastReceivedValue;

SoftwareSerial bluetoothSerial(0, 1); // RX, TX pins for HC-06

// === Remote setup ===
const char* commands[] = {
  "bright", "dim", "pause", "power",
  "red", "green", "blue", "white",
  "red1", "green1", "blue1", "white1",
  "red2", "green2", "blue2", "white2",
  "red3", "green3", "blue3", "white3",
  "red4", "green4", "blue4", "white4",
  "red_up", "green_up", "blue_up", "quick",
  "red_down", "green_down", "blue_down", "slow",
  "diy1", "diy2", "diy3", "autom",
  "diy4", "diy5", "diy6", "flash",
  "jump3", "jump7", "fade3", "fade7"
};

const uint16_t remoteCodes[] = {
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

void setup() {
  Wire.begin();                 // Initialize I2C
  Serial.begin(9600);           // Initialize Serial Monitor
  bluetoothSerial.begin(9600);  // Initialize Bluetooth serial communication
}

void loop() {
  if (bluetoothSerial.available()) {
    String receivedString = bluetoothSerial.readStringUntil('\n');  // Read the string from Bluetooth
    receivedString.trim();  // Remove leading/trailing whitespaces

    uint16_t remoteCode = getRemoteCode(receivedString);
    if (remoteCode != 0) {
      sendRemoteCode(remoteCode);
      Serial.print("Sent value over I2C: ");
      Serial.println(remoteCode);
    } else {
      Serial.println("Invalid command");
    }
  }
}

uint16_t getRemoteCode(const String& command) {
  for (size_t i = 0; i < sizeof(commands) / sizeof(commands[0]); ++i) {
    if (command == commands[i]) {
      return remoteCodes[i];
    }
  }
  return 0; // Return 0 if the command is not found
}

void sendRemoteCode(uint16_t code) {
  if (code != lastReceivedValue) {
    lastReceivedValue = code;
    Wire.beginTransmission(9);      // I2C address of the receiver device
    Wire.write(code);  // Send the value over I2C
    Wire.endTransmission();
  }
}