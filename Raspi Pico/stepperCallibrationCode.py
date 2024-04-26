import machine
import utime

# GPIO pins connected to the ULN2003 driver board
stepper_pins = [machine.Pin(i, machine.Pin.OUT) for i in range(14, 18)]

# 28BYJ-48 stepping sequence
step_sequence = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
]

def set_step(sequence):
    for i in range(4):
        stepper_pins[i].value(sequence[i])

def rotate_motor(steps, delay):
    for _ in range(steps):
        for sequence in step_sequence:
            set_step(sequence)
            utime.sleep_ms(delay)

def main():
    steps_per_full_rotation = 512
    steps_per_point = steps_per_full_rotation // 12

    for point in range(1, 13):
        rotate_motor(steps_per_point, 10)
        print(point)
        utime.sleep(1)  # Wait for a second at each point

if __name__ == '__main__':
    main()
