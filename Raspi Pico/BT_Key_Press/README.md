# Pico W Bluetooth Button Controller

A beginner-friendly project: turn a **Raspberry Pi Pico W** into a Bluetooth keyboard with two push buttons.

| Button | Pico connection | Sends |
|---|---|---|
| Button A | GP16 (physical pin 21) to GND | `a` |
| Button B | GP15 (physical pin 20) to GND | `b` |

Each press sends **one** character. You can test it in Notepad or use the keys to control another application.

## What you'll need

- Raspberry Pi **Pico W** (or Pico 2 W, selected appropriately in Arduino IDE); a standard Pico without **W** does **not** have Bluetooth.
- Data-capable micro-USB cable (not a charge-only cable)
- Two momentary push buttons
- Breadboard and jumper wires (or other secure connections)
- Windows, macOS, or Linux computer with Bluetooth for pairing

## Step 1: Install Arduino IDE

1. Download and install **Arduino IDE 2** from <https://www.arduino.cc/en/software>.
2. Start Arduino IDE.
3. Go to **File → Preferences** (on macOS, Arduino IDE → Settings).
4. In **Additional Boards Manager URLs**, paste:

   ```text
   https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json
   ```

   If there is already a URL there, add this one as an additional entry.
5. Click **OK**.
6. Open **Tools → Board → Boards Manager**, search for `pico`, and install **Raspberry Pi Pico/RP2040 by Earle F. Philhower, III**. Wait for installation to finish.

> **Important:** Choose the *Earle Philhower* board package for this lesson because it provides `KeyboardBLE.h`. Do not confuse it with a similarly named board package.

## Step 2: Select your Pico board and enable Bluetooth

1. Go to **Tools → Board → Raspberry Pi Pico/RP2040 → Raspberry Pi Pico W**. If using a Pico 2 W, select **Raspberry Pi Pico 2 W** instead.
2. Go to **Tools → IP/Bluetooth Stack** and select a setting that **enables Bluetooth** (normally **IPv4 + Bluetooth**). The exact wording varies by core version. Do not leave Bluetooth disabled.

The `KeyboardBLE` library is included with the Earle Philhower Pico core, so **no separate KeyboardBLE download is needed**.

## Step 3: Connect the buttons

**Unplug the Pico before wiring.**

```text
    BUTTON A                        BUTTON B
     ┌─────┐                         ┌─────┐
GP16 ─┤     ├─ GND             GP15 ──┤     ├─ GND
     └─────┘                         └─────┘
```

- **Button A:** one side to **GP16**, physical pin **21**; the other side to **GND**.
- **Button B:** one side to **GP15**, physical pin **20**; the other side to **GND**.
- You can share a GND connection between both buttons.
- The code uses `INPUT_PULLUP`, so **external resistors are not needed**.
- On typical four-legged tactile switches, the two legs **on the same side are already connected**. Use legs from opposite sides of the switch, or check with a continuity tester.
- Do not connect the buttons to 3.3V or 5V for this particular wiring arrangement.

Pico official pinout: <https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf>.

## Step 4: Paste in the code

In Arduino IDE, select **File → New Sketch**, delete the default template, and paste the following:

```cpp
#include <KeyboardBLE.h>

const int buttonA = 16;  // GP16 sends 'a'
const int buttonB = 15;  // GP15 sends 'b'

bool lastA = HIGH;
bool lastB = HIGH;

void setup() {
  Serial.begin(115200);

  // A button connects the GPIO to GND when pressed.
  pinMode(buttonA, INPUT_PULLUP);
  pinMode(buttonB, INPUT_PULLUP);

  KeyboardBLE.begin("Student Controller");
  Serial.println("Bluetooth controller ready!");
}

void loop() {
  bool currentA = digitalRead(buttonA);
  bool currentB = digitalRead(buttonB);

  // Detect the transition from released to pressed.
  if (currentA == LOW && lastA == HIGH) {
    KeyboardBLE.write('a');
    Serial.println("Button A: sent a");
  }

  if (currentB == LOW && lastB == HIGH) {
    KeyboardBLE.write('b');
    Serial.println("Button B: sent b");
  }

  lastA = currentA;
  lastB = currentB;

  // Basic switch debounce. Good for the first classroom project.
  delay(30);
}
```

**Note:** A physical switch may sometimes generate extra presses due to mechanical bounce. This sketch uses a simple 30 ms delay; for more demanding projects, use per-button timed debouncing.

## Step 5: Plug in and upload to the Pico W

For a **first upload**, or if the normal upload fails:

1. **Unplug** the Pico W from the computer.
2. **Hold down BOOTSEL** (the white button on the Pico board).
3. While holding BOOTSEL, **plug in the micro-USB cable**.
4. Release BOOTSEL. The computer should show a removable drive called **RPI-RP2**.
5. In Arduino IDE, check that the correct **Pico W** board is selected.
6. Click **Upload** (the right-arrow button). Allow the IDE time to compile and transfer the program. The RPI-RP2 drive should disappear when the Pico starts running the sketch.

After the first upload, later uploads can usually be done normally if you select the Pico's serial port under **Tools → Port**. If it gets stuck, repeat the BOOTSEL method.

> A newly plugged-in Pico showing up only as **RPI-RP2** is normal during BOOTSEL mode. It may not initially show a regular serial port.

## Step 6: Pair the Pico over Bluetooth

1. Leave the Pico powered by USB. USB provides power; the keypresses are transmitted over **Bluetooth**, not through the USB cable.
2. On **Windows 11**, open **Settings → Bluetooth & devices → Add device → Bluetooth**. On Windows 10, use **Settings → Devices → Bluetooth & other devices → Add Bluetooth or other device**.
3. Find and select **Student Controller**.
4. Wait until Windows reports that it is connected or paired.

If it does not appear, check the **Tools → IP/Bluetooth Stack** setting, ensure the sketch uploaded successfully, and try switching Bluetooth off and on in Windows. If you previously paired a Pico under another name, remove the old paired device and pair again.

## Step 7: Test it

1. Open **Notepad** (or any plain text editor).
2. Click inside the document so it has keyboard focus.
3. Press **Button A**. You should see `a`.
4. Press **Button B**. You should see `b`.
5. Try alternating the buttons. You should see something like `abba`.

To see debugging output while the Pico is plugged into USB, open **Tools → Serial Monitor** and set **115200 baud**.

## Troubleshooting

| Problem | What to check |
|---|---|
| The computer doesn't detect the Pico during upload | Use a **data** cable; try the **BOOTSEL** upload method; verify the correct board is selected. |
| `KeyboardBLE.h: No such file or directory` | Install/select **Raspberry Pi Pico/RP2040 by Earle Philhower**, not a different Pico core. |
| Bluetooth device doesn't appear | Ensure you selected **Pico W**, enabled a **Bluetooth-capable IP/Bluetooth Stack**, uploaded successfully, and kept USB power connected. |
| Button does nothing | Check GP16/GP15 **GPIO numbers**, GND, and button leg placement. |
| Buttons type without being pressed | Look for an unintended short to GND, often from wiring the same side of a four-leg switch. |
| One press sometimes types twice | Mechanical switch bounce. Try proper `millis()`-based debouncing as an extension. |
| Paired but no text appears | Click inside Notepad; check connection status; try removing and re-pairing the device. |

## Student challenges

1. Change the Bluetooth name from `Student Controller` to your own controller name.
2. Change the output to **left** and **right** arrow keys using `KEY_LEFT_ARROW` and `KEY_RIGHT_ARROW`.
3. Add a third button on another GPIO pin.
4. Build a two-player quiz buzzer or a simple game controller.
5. Improve the button debouncing without using `delay()`.

## Useful references

- [Arduino IDE downloads](https://www.arduino.cc/en/software)
- [Earle Philhower Pico core installation](https://arduino-pico.readthedocs.io/en/stable/install.html)
- [Bluetooth on Pico W: stack setting and `KeyboardBLE`](https://arduino-pico.readthedocs.io/en/stable/bluetooth.html)
- [Official Raspberry Pi Pico pinout](https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf)
