import RPi.GPIO as GPIO
import time

class Light:
    def __init__(self):
        self.outputs = [20, 21]
        # inputs = []
        GPIO.setmode(GPIO.BCM)

        for pin in self.outputs:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

        # for pin in inputs:
        #     GPIO.setup(pin, GPIO.IN)

    def setOutputs(self):
        for pin in self.outputs:
            GPIO.output(pin, GPIO.HIGH)

    @staticmethod
    def main():
        light = Light()
        light.setOutputs()
    
if __name__ == "__main__":
    try:
        print("Initializing light system...")
        Light.main()
        print("Lights are ON. Press Ctrl+C to exit.")
        while True:
            time.sleep(20)
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    finally:
        GPIO.cleanup()


