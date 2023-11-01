import network
import time
import utime
import ntptime
import datetime
import urequests

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    if wlan.isconnected():
        print("Online")
    else:
        print("Error connecting to WiFi")

def get_time():
    response = urequests.get("http://worldtimeapi.org/api/timezone/Europe/London")
    json_data = response.json()
    datetime_str = json_data['datetime']  # format: "2023-11-01T12:34:56.789123+00:00"
    hour = int(datetime_str[11:13])
    return hour


if __name__ == "__main__":
    ssid = "x"
    password = "x"

    connect_to_wifi(ssid, password)

    if network.WLAN(network.STA_IF).isconnected():
        hour = get_time()
        
        print("Current time: {}:00".format(hour))
        
        if 19 <= hour or hour < 7:
            print("Red for Bed")
        elif 7 <= hour < 8:
            print("Orange for getting up")
        else:
            print("Day time blue")
        
        utime.sleep(60)  # wait for 60 seconds before checking again
        
    else:
        print("Not connected to WiFi")
