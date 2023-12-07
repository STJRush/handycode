from time import sleep
from machine import SoftI2C, Pin
from utime import ticks_diff, ticks_us

from max30102 import MAX30102, MAX30105_PULSE_AMP_MEDIUM





def main():
    # I2C software instance
    i2c = SoftI2C(sda=Pin(16),  # Here, use your I2C SDA pin
                  scl=Pin(17),  # Here, use your I2C SCL pin
                  freq=400000)  # Fast: 400kHz, slow: 100kHz

    # Sensor instance
    sensor = MAX30102(i2c=i2c)
    previous_HR = 72

    # Scan I2C bus to ensure that the sensor is connected
    if sensor.i2c_address not in i2c.scan():
        print("Sensor not found. oose wire? Stop and start again.")
        return
    elif not (sensor.check_part_id()):
        print("I2C device ID not corresponding to MAX30102 or MAX30105. Loose wire? Stop and start again.")
        return
    else:
        print("Sensor connected and recognized.")
        print("Place the pad of your middle finger on the sensor and hold it still")
        print("You should see a sine wave under VIEW>PLOTTER on Thonny or move until you get a steady wave")
        print("HR is measured every 8 peaks")
        sleep(2)

    print("Setting up sensor with default configuration.", '\n')
    sensor.setup_sensor()

    sensor.set_sample_rate(400)
    sensor.set_fifo_average(8)
    sensor.set_active_leds_amplitude(MAX30105_PULSE_AMP_MEDIUM)

    sleep(1)

    print("Reading temperature in °C.", '\n')
    print(sensor.read_temperature())

    print("Starting data acquisition from RED & IR registers...", '\n')
    sleep(1)

    # Heart Rate Calculation
    last_peak_time = 0
    peak_interval_sum = 0
    peak_count = 0

    # Variables for trend detection
    increasing = False
    decreasing = False
    last_ir_reading = 0

    # Increase the number of peaks required to calculate the heart rate
    required_peaks = 8

    while True:
        sensor.check()

        if sensor.available():
            red_reading = sensor.pop_red_from_storage()
            ir_reading = sensor.pop_ir_from_storage()
            #print(red_reading, ",", ir_reading)
            print(ir_reading-14500)
            # Trend detection for peak
            if ir_reading > last_ir_reading:
                increasing = True
                if decreasing:  # A peak is detected
                    current_time = ticks_us()
                    if last_peak_time != 0:
                        interval = ticks_diff(current_time, last_peak_time)
                        peak_interval_sum += interval
                        peak_count += 1

                        if peak_count >= required_peaks:
                            average_interval = peak_interval_sum / peak_count
                            heart_rate = 60 / (average_interval / 1000000)
                            
                            
                            if (previous_HR - heart_rate > 10) or (heart_rate >130):
                                print("Tikes! Too big a jump in Heart Rate! Probably a bad reading!")
                                print("Reposition the LED under the pad of your middle finger and hold still")
                                sleep(2)
                            else: 
                                print("Heart Rate: {:.2f} BPM".format(heart_rate))
                                sleep(1)

                            # Reset for next calculation
                            peak_interval_sum = 0
                            peak_count = 0
                            previous_HR = heart_rate

                    last_peak_time = current_time

                decreasing = False
            elif ir_reading < last_ir_reading and increasing:
                decreasing = True

            last_ir_reading = ir_reading

if __name__ == '__main__':
    main()
