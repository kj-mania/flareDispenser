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
        for pin in self.outputs:
            GPIO.output(pin, GPIO.HIGH)
            print(f"Turning on output on pin {pin}")

    def checkInputs(self):
        for pin in self.inputs:
            if GPIO.input(pin):
                print(GPIO.input(pin))
                print(f"Input on pin {pin} is HIGH")
            else:
                print(f"Input on pin {pin} is LOW")

    @staticmethod
    def main():
        light = Light()
        light.lightOutputs()
        light.checkInputs()
    
if __name__ == "__main__":
    try:
        print("Initializing light system...")
        time.sleep(2)
        Light.main()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    finally:
        GPIO.cleanup()

