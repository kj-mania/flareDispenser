import RPi.GPIO as GPIO
import time

class Light:

    def __init__(self, outputs: list, inputs: list, red: int, blue: int):
        self.outputs = outputs
        self.inputs = inputs
        self.red = red
        self.blue = blue

        GPIO.setmode(GPIO.BCM)

        for pin in self.outputs:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

        GPIO.setup(self.red, GPIO.OUT)
        GPIO.output(self.red, GPIO.LOW)
        GPIO.setup(self.blue, GPIO.OUT)
        GPIO.output(self.blue, GPIO.LOW)
        
        for pin in self.inputs:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def activate(self, pin: int):
        return GPIO.output(pin, GPIO.HIGH)
    
    def deactivate(self, pin: int):
        return GPIO.output(pin, GPIO.LOW)
    
    def inputOn(self, pin: int) -> bool:
        return GPIO.input(pin)
    
    @staticmethod
    def cleanup(self):
        GPIO.cleanup()
