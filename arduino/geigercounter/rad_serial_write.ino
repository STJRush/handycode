#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <SPI.h>

#define LOG_PERIOD 15000
#define MAX_PERIOD 60000

unsigned long counts;
unsigned long cpm;
unsigned int multiplier;
unsigned long previousMillis;
float usv;

LiquidCrystal_I2C lcd(0x27, 16, 2);

void tube_impulse() {
  counts++;
}

void setup() {
  counts = 0;
  cpm = 0;
  multiplier = MAX_PERIOD / LOG_PERIOD;

  Serial.begin(9600);
  attachInterrupt(0, tube_impulse, FALLING);

  lcd.init();
  lcd.backlight();
  lcd.setCursor(5, 0);
  lcd.print("Boot...");
  lcd.setCursor(0, 1);
  for(int i = 0; i < 16; i++) {
    lcd.write(0xff);
    delay(250);
  }
}

void loop() {
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis > LOG_PERIOD) {
    previousMillis = currentMillis;
    cpm = counts * multiplier;
    usv = float(cpm) / 151;
    counts = 0;

    // Print to LCD
    lcd.clear();
    lcd.print("CPM=");
    lcd.print(cpm);
    lcd.setCursor(0, 1);
    lcd.print(usv);
    lcd.print(" uSv/h");

    // Print to Serial as CSV: cpm,usv
    Serial.print(cpm);
    Serial.print(",");
    Serial.println(usv);

    // Check radiation levels
    if (usv >= 10) {
      lcd.setCursor(9, 0);
      lcd.print("Danger!");
      delay(0.1);
    }
    else if (usv < 10 && usv >= 0.52) {
      lcd.setCursor(10, 0);
      lcd.print("Unsafe");
      delay(0.1);
    }
    else if (usv < 0.52) {
      lcd.setCursor(10, 0);
      lcd.print("Safety");
      delay(0.1);
    }
  }
}
