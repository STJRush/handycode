from machine import Pin, ADC, PWM
import utime

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
    ad_value = adc.read_u16()
    print("ADC reading:", ad_value)
    
    # Compute the delay period based on the current sensor reading
    period = compute_beep_period(ad_value)
    
    # Define the beep (tone) duration; if period is very short, beep continuously.
    beep_duration = 0.05  # seconds
    if period <= beep_duration:
        # For very high UV levels: continuous tone
        buzzer.duty_u16(32768)  # 50% duty cycle to generate tone
        utime.sleep(period)
    else:
        # Beep for the specified duration, then pause for the remainder of the period.
        buzzer.duty_u16(32768)  # Turn on buzzer
        utime.sleep(beep_duration)
        buzzer.duty_u16(0)      # Turn off buzzer
        utime.sleep(period - beep_duration)
