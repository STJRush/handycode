from sense_hat import SenseHat

sh = SenseHat()
temperature = sh.get_temperature()
print(temperature)

sh.show_message("Its" + str(temperature) + "C")
