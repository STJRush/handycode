
#include <KeyboardBLE.h>

// Button pins
const int buttonA = 16;
const int buttonB = 15;

// Remember the previous button states
bool lastA = HIGH;
bool lastB = HIGH;

void setup() {
  // Start serial monitor
  Serial.begin(115200);

  // Enable internal pull-up resistors
  pinMode(buttonA, INPUT_PULLUP);
  pinMode(buttonB, INPUT_PULLUP);

  // Start Bluetooth keyboard
  KeyboardBLE.begin("Student Controller");

  Serial.println("Bluetooth controller ready!");
}

void loop() {
  // Read both buttons
  bool currentA = digitalRead(buttonA);
  bool currentB = digitalRead(buttonB);

  // Button A pressed
  if (currentA == LOW && lastA == HIGH) {
    KeyboardBLE.write('a');
    Serial.println("Button A pressed");
  }

  // Button B pressed
  if (currentB == LOW && lastB == HIGH) {
    KeyboardBLE.write('b');
    Serial.println("Button B pressed");
  }

  // Save button states
  lastA = currentA;
  lastB = currentB;

  // Small delay for basic debouncing
  delay(30);
}
