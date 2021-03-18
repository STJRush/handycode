# Python program to find current 
# weather details of any city 
# using openweathermap api 

# 0K = 273.15 °C


# import required modules 
import requests, json 

# Enter your API key here. Uf you're using this in a progect, you should sign up and get your OWN API key. This one is Kevin's. 

api_key = "a19c355c905cbcb821b784d45a9cb1de"

# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name 
city_name = "Rush"

# complete_url variable to store 
# complete url address 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

# get method of requests module 
# return response object 
response = requests.get(complete_url) 

# json method of response object 
# convert json format data into 
# python format data 
x = response.json() 


"""play with this to see the raw, full output from the data stream"""
# print(x)  

# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if x["cod"] != "404": 

	# store the value of "main" 
	# key in variable y 
	y = x["main"] 

	#print(y)

	# store the value corresponding 
	# to the "temp" key of y 
	current_temperature = y["temp"] 

	# store the value corresponding 
	# to the "pressure" key of y 
	current_pressure = y["pressure"] 

	# store the value corresponding 
	# to the "humidity" key of y 
	current_humidiy = y["humidity"] 

	# store the value of "weather" 
	# key in variable z 
	z = x["weather"]

	# store the value corresponding 
	# to the "description" key at 
	# the 0th index of z 
	weather_description = z[0]["description"] 


# Here are those outputs printed very plainly so that you can use them

print(current_temperature)
print(current_pressure)
print(current_humidiy)
print(weather_description)


# Things to do:

# Displaty the temperature in °C instead of kelvin (subtract 273.15)

# Round this number using: whatYouWant = round(number_to_round, 2)   That's 2 decimal places.


# COVID SAFETY ALARM IDEA:

# Run this program on a Raspberri Pi. Use a DHT sensor to measure the actual room temperature indoors.

# Compare the Room Temperature to the Outside Weathermap Temperature. If the room temperature is 23°C and the outside temperature is 4°C then someone is very wrong. There is no way those classroom windows could be open (unless you're burning a fire indoors). You should notify the students in the room with an alarm sound or bright flashy LED lights! They're in a poorly ventilated area!
