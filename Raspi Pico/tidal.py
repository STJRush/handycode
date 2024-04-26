import network
import ntptime
import machine
import utime

# Stepper motor and buttons setup
stepper_pins = [machine.Pin(i, machine.Pin.OUT) for i in range(14, 18)]
button_forward = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)
button_backward = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)
step_sequence = [
    [1,0,0,0], [1,1,0,0], [0,1,0,0], [0,1,1,0],
    [0,0,1,0], [0,0,1,1], [0,0,0,1], [1,0,0,1]
]

# Function definitions
def set_step(sequence):
    for i in range(4):
        stepper_pins[i].value(sequence[i])

def rotate_motor(steps, delay, direction='forward'):
    sequence = step_sequence if direction == 'forward' else reversed(step_sequence)
    for _ in range(abs(steps)):
        for step in sequence:
            set_step(step)
            utime.sleep_ms(delay)

def center_dial():
    print("Adjust dial using buttons, press both to confirm centering.")
    while True:
        forward_pressed = not button_forward.value()
        backward_pressed = not button_backward.value()
        if forward_pressed and backward_pressed:
            print("Dial centered")
            break
        elif forward_pressed:
            rotate_motor(1, 10, 'forward')
            utime.sleep(0.2)
        elif backward_pressed:
            rotate_motor(1, 10, 'backward')
            utime.sleep(0.2)

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to WiFi...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print("Connected to WiFi")
    print("Network config:", wlan.ifconfig())

def sync_time_with_ntp():
    try:
        ntptime.settime()  # Synchronize the system time with NTP server
        current_time = utime.localtime()
        print("Current time:", current_time)
        return current_time
    except:
        print("Could not synchronize with NTP server")
        return None

# WiFi credentials
ssid = 'Funtrap'
password = 'jumpinthesea'

# Connect to WiFi and synchronize time
connect_to_wifi(ssid, password)
current_time = sync_time_with_ntp()

# Rest of the tide clock logic goes here...
# Note: You'll need to adjust the tide clock logic to work with the synchronized time

# Allow user to center the dial using buttons
center_dial()

# Example: Rotate the stepper motor based on the current time
# You'll need to implement the logic for moving the stepper based on the tide data
