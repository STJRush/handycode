serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE115200)
serial.redirect_to_usb()

def on_forever():
    serial.write_number(input.temperature())
    serial.write_line("")
    basic.show_number(input.temperature())
    basic.pause(5000)
basic.forever(on_forever)
