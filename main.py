intensité = 0
def green():
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 0)
    pins.digital_write_pin(DigitalPin.P8, 1)
def blue():
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 1)
    pins.digital_write_pin(DigitalPin.P3, 0)
def red():
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 0)
    pins.digital_write_pin(DigitalPin.P8, 0)

def on_forever():
    global intensité
    intensité = pins.digital_read_pin(DigitalPin.P0)
    if intensité >= 700:
        green()
    elif intensité < 700:
        blue()
    else:
        red()
basic.forever(on_forever)
