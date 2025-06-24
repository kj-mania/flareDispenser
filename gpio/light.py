import RPi.GPIO as GPIO
import time

class Light:

    def __init__(self, outputs: list, inputs: list):
        self.outputs = outputs
        self.inputs = inputs

        GPIO.setmode(GPIO.BCM)

        for pin in self.outputs:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

        for pin in self.inputs:
            GPIO.setup(pin, GPIO.IN)

    
    def outputOn(pin: int) -> bool:
        return GPIO.output(pin, GPIO.HIGH)
    
    def outputOff(pin: int) -> bool:
        return GPIO.output(pin, GPIO.LOW)
    
    def inputOn(pin: int) -> bool:
        return GPIO.input(pin)
