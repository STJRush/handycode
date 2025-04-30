from machine import Pin, I2C
import utime

# DS3231 RTC class for zs-042 RTC module
class DS3231:
    def __init__(self, i2c, addr=0x68):
        self.i2c = i2c
        self.addr = addr

    def dec2bcd(self, dec):
        return ((dec // 10) << 4) | (dec % 10)
    
    def bcd2dec(self, bcd):
        return (bcd >> 4) * 10 + (bcd & 0x0F)
    
    def set_time(self, year, month, day, hour, minute, second, weekday=1):
        """
        Set the time on the RTC.
        year: Full year (e.g., 2025)
        month: Month (1-12)
        day: Day of month (1-31)
        hour: Hour in 24-hour format (0-23)
        minute: Minute (0-59)
        second: Second (0-59)
        weekday: Day of week (1-7), default is 1 if not calculated
        """
        # Convert values to BCD format
        second_bcd = self.dec2bcd(second) & 0x7F  # Ensure the CH (clock halt) bit is 0
        minute_bcd = self.dec2bcd(minute)
        hour_bcd = self.dec2bcd(hour)  # 24-hour mode assumed
        weekday_bcd = self.dec2bcd(weekday)
        day_bcd = self.dec2bcd(day)
        month_bcd = self.dec2bcd(month)
        year_bcd = self.dec2bcd(year - 2000)  # DS3231 stores year as offset from 2000

        # Prepare the data array for registers 0x00 to 0x06
        data = bytearray([second_bcd, minute_bcd, hour_bcd, weekday_bcd, day_bcd, month_bcd, year_bcd])
        self.i2c.writeto_mem(self.addr, 0x00, data)
    
    def get_time(self):
        # Read 7 bytes starting from register 0x00
        data = self.i2c.readfrom_mem(self.addr, 0x00, 7)
        second = self.bcd2dec(data[0] & 0x7F)
        minute = self.bcd2dec(data[1])
        hour = self.bcd2dec(data[2])
        weekday = self.bcd2dec(data[3])
        day = self.bcd2dec(data[4])
        month = self.bcd2dec(data[5] & 0x1F)
        year = self.bcd2dec(data[6]) + 2000
        return (year, month, day, hour, minute, second, weekday)
    
    def get_time_str(self):
        t = self.get_time()
        return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(t[0], t[1], t[2], t[3], t[4], t[5])

# Setup I2C for RTC on GP16 (SDA) and GP17 (SCL)
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
rtc = DS3231(i2c)

def main():
    print("Current RTC time:", rtc.get_time_str())
    print("Enter new time in format YYYY-MM-DD HH:MM:SS")
    time_str = input("New time: ")
    try:
        date_str, time_part = time_str.strip().split(" ")
        year, month, day = [int(x) for x in date_str.split("-")]
        hour, minute, second = [int(x) for x in time_part.split(":")]
    except Exception as e:
        print("Invalid format. Please use 'YYYY-MM-DD HH:MM:SS'")
        return

    # For simplicity, we use a default weekday value of 1.
    weekday = 1

    rtc.set_time(year, month, day, hour, minute, second, weekday)
    utime.sleep(1)  # Allow time for the RTC to update
    print("RTC time updated to:", rtc.get_time_str())

if __name__ == "__main__":
    main()
