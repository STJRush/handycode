def on_button_pressed_a():
    global switch_position
    switch_position = 0
    basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global switch_position
    switch_position = 1
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.B, on_button_pressed_b)

switch_position = 0
serial.redirect_to_usb()

def on_forever():
    basic.show_number(input.temperature())
    serial.write_line("" + str((input.temperature())))
    serial.write_line("" + str((switch_position)))
    basic.pause(1000)
basic.forever(on_forever)
