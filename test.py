import RPi.GPIO as GPIO
import time

class Light:
    def __init__(self):
        self.outputs = 21
        
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.outputs, GPIO.OUT)
        GPIO.output(self.outputs, GPIO.LOW)

    def lightOutputs(self):
        GPIO.output(self.outputs, GPIO.LOW)
        print("Lighting outputs...")
        print(f"Turning on output on pin {self.outputs}")
        GPIO.output(self.outputs, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(self.outputs, GPIO.LOW)

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
        # light.checkAllInputs()
    
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

