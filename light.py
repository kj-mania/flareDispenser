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
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def activate(self, pin: int) -> bool:
        return GPIO.output(pin, GPIO.HIGH)
    
    def deactivate(self, pin: int) -> bool:
        return GPIO.output(pin, GPIO.LOW)
    
    def inputOn(self, pin: int) -> bool:
        return GPIO.input(pin)
    
    def cleanup(self):
        GPIO.cleanup()
