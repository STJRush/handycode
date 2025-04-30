from machine import Pin, ADC, PWM, I2C
import utime

# DS3231 RTC class for zs-042 RTC module
class DS3231:
    def __init__(self, i2c, addr=0x68):
        self.i2c = i2c
        self.addr = addr

    def bcd2dec(self, bcd):
        return (bcd >> 4) * 10 + (bcd & 0x0F)

    def get_time(self):
        # Read 7 bytes starting at register 0x00
        data = self.i2c.readfrom_mem(self.addr, 0x00, 7)
        sec = self.bcd2dec(data[0] & 0x7F)
        minute = self.bcd2dec(data[1])
        hour = self.bcd2dec(data[2])
        day = self.bcd2dec(data[4])
        month = self.bcd2dec(data[5] & 0x1F)
        year = self.bcd2dec(data[6]) + 2000
        return (year, month, day, hour, minute, sec)

    def get_time_str(self):
        t = self.get_time()
        return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(t[0], t[1], t[2], t[3], t[4], t[5])

# Setup I2C for RTC on GP16 (SDA) and GP17 (SCL)
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
rtc = DS3231(i2c)

# Setup ADC for UV sensor on GPIO26
adc = ADC(0)

# Setup buzzer PWM on GPIO0
buzzer = PWM(Pin(0))
buzzer.freq(2000)  # Set tone frequency to 2kHz

def compute_beep_period(ad_value):
    """
    Map the sensor reading (range ~20 to 900) to a beep period (delay)
    where a lower reading gives a longer delay (slower beeping)
    and a higher reading gives a shorter delay (faster beeping).
    """
    min_reading = 20
    max_reading = 900
    max_delay = 1.0   # seconds delay at low UV levels
    min_delay = 0.1   # seconds delay at high UV levels

    # Clamp the sensor value within expected range
    if ad_value < min_reading:
        ad_value = min_reading
    if ad_value > max_reading:
        ad_value = max_reading

    # Linear mapping: Higher sensor value reduces the delay
    period = max_delay - (ad_value - min_reading) * (max_delay - min_delay) / (max_reading - min_reading)
    return period

while True:
    # Read the UV sensor value
    ad_value = adc.read_u16()
    # Get the current time from the RTC
    timestamp = rtc.get_time_str()
    print("Time:", timestamp, "ADC reading:", ad_value)
    
    # Log the timestamp and sensor value to uvdata.csv
    with open("uvdata.csv", "a") as f:
        f.write("{},{}\n".format(timestamp, ad_value))
    
    # Compute the delay period for beeping based on the sensor reading
    period = compute_beep_period(ad_value)
    beep_duration = 0.05  # seconds for which the buzzer is on

    if period <= beep_duration:
        # For very high UV levels: nearly continuous tone
        buzzer.duty_u16(32768)  # Turn on buzzer at 50% duty cycle
        utime.sleep(period)
    else:
        # Beep for beep_duration, then pause for the remainder of the period
        buzzer.duty_u16(32768)  # Turn on buzzer
        utime.sleep(beep_duration)
        buzzer.duty_u16(0)      # Turn off buzzer
        utime.sleep(period - beep_duration)
