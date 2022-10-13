import network
import secrets
import time
import urequests
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)
print(wlan.isconnected())

ufirestore.set_project_id("rpitempdata")
ufirestore.set_access_token("INSERT_ACCESS_TOKEN")
raw_doc = ufirestore.get("DOCUMENT_PATH")
doc = FirebaseJson.from_raw(raw_doc)

if doc["fields"].exists("FIELD"):
    print("The field value is: %s" % doc["fields"].get("FIELD"))
