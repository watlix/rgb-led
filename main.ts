let intensité = 0
function green () {
    pins.digitalWritePin(DigitalPin.P1, 1)
    pins.digitalWritePin(DigitalPin.P2, 1)
    pins.digitalWritePin(DigitalPin.P8, 0)
}
function PURPO () {
    pins.digitalWritePin(DigitalPin.P1, 1)
    pins.digitalWritePin(DigitalPin.P2, 0)
    pins.digitalWritePin(DigitalPin.P8, 1)
}
function blaNBS46I () {
    pins.digitalWritePin(DigitalPin.P1, 1)
    pins.digitalWritePin(DigitalPin.P2, 1)
    pins.digitalWritePin(DigitalPin.P8, 1)
}
function blue () {
    pins.digitalWritePin(DigitalPin.P1, 0)
    pins.digitalWritePin(DigitalPin.P2, 0)
    pins.digitalWritePin(DigitalPin.P8, 1)
}
function red () {
    pins.digitalWritePin(DigitalPin.P1, 1)
    pins.digitalWritePin(DigitalPin.P2, 0)
    pins.digitalWritePin(DigitalPin.P8, 0)
}
basic.forever(function () {
    basic.showNumber(intensité)
    intensité = pins.analogReadPin(AnalogPin.P0)
    if (intensité <= 800 && intensité > 600) {
        red()
    } else if (intensité <= 600 && intensité > 400) {
        blue()
    } else if (intensité <= 400 && intensité > 200) {
        PURPO()
    } else if (intensité <= 200 && intensité >= 130) {
        green()
    } else {
        blaNBS46I()
    }
})
