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


        # for pin in inputs:
        #     GPIO.setup(pin, GPIO.IN)

    def lightOutputs(self):
        print("Lighting outputs...")
        for pin in self.outputs:
            print(f"Turning on output on pin {pin}")
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(5)

    def checkAllInputs(self) -> bool:
        flaresWentOff = 0
        for pin in self.inputs:
            print(f"Checking input on pin {pin}")
            if GPIO.input(pin) == GPIO.HIGH:
                flaresWentOff += 1
                print(f"Input on pin {pin} is HIGH, flare went off!")
        return flaresWentOff == len(self.inputs)

    @staticmethod
    def main():
        light = Light()
        light.lightOutputs()
        light.checkAllInputs()
    
if __name__ == "__main__":
    try:
        print("Initializing light system...")
        Light.main()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    finally:
        GPIO.cleanup()


