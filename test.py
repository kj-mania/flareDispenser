import RPi.GPIO as GPIO
import time

class Light:
    def __init__(self):
        self.outputs = [21, 20]
        self.inputs = [26, 19]
        GPIO.setmode(GPIO.BCM)

        for pin in self.outputs:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

        for pin in self.inputs:
            GPIO.setup(pin, GPIO.IN)

    def lightOutputs(self):
        print("Lighting outputs 21 and 20")
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(20, GPIO.HIGH)

    def checkInputs(self):
        for pin in self.inputs:
            if GPIO.input(pin):
                print(f"Input on pin {pin} is HIGH, flare went off!")
            else:
                print(f"Input on pin {pin} is LOW, flare did not go off.")

    @staticmethod
    def main():
        light = Light()
        light.lightOutputs()
        light.checkInputs()
    
if __name__ == "__main__":
    try:
        print("Initializing light system...")
        time.sleep(5)
        Light.main()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    finally:
        GPIO.cleanup()

