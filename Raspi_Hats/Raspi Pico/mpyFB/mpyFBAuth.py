import network
import time
from firebase_auth import FirebaseAuth

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    wlan.connect("Valar Morghulis", "valardohaeris")
    print("Waiting for Wi-Fi connection", end="...")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
    print()
print("got here")
from WifiModCloud import WifiModCloud
import time

print("got here now")
wmc = WifiModCloud() 
wmc.setdb_to_firebase(host="https://rpitempdata.firebaseio.com/", auth="AIzaSyAG9BsCVxnghtBKlplqEKDPmWkFS-m0eUU", tree="R12") 
print("got here1")
wmc.set_value(key="Mynumber", value = 2.21)
print("got here2")
time.sleep(10)
print("got here3")
get_value=wmc.get_value(key="Mynumber")
print("got here6")

"""
api_key = "AIzaSyAG9BsCVxnghtBKlplqEKDPmWkFS-m0eUU"
auth = FirebaseAuth(api_key)
response = auth.sign_in("dcuish@gmail.com", "Pass1234")


auth.user: dict()
print("Hello, " + auth.user.display_name)
#auth.session: AuthSession
#session.request(method, endpoint, data=None, method=None, **kwargs)
#session.access_token
"""