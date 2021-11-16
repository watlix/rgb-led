intensité = 0
def green():
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 1)
    pins.digital_write_pin(DigitalPin.P8, 0)
def PURPO():
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 0)
    pins.digital_write_pin(DigitalPin.P8, 1)
def blaNBS46I():
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 1)
    pins.digital_write_pin(DigitalPin.P8, 1)
def blue():
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 0)
    pins.digital_write_pin(DigitalPin.P8, 1)
def red():
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 0)
    pins.digital_write_pin(DigitalPin.P8, 0)

def on_forever():
    global intensité
    intensité = pins.digital_read_pin(DigitalPin.P0)
    if intensité <= 800 and intensité > 600:
        red()
    elif intensité <= 600 and intensité > 400:
        blue()
    elif intensité <= 400 and intensité > 200:
        PURPO()
    elif intensité <= 200 and intensité >= 1:
        green()
    else:
        blaNBS46I()
basic.forever(on_forever)
