import RPi.GPIO as GPIO
import time

class Light:
    def __init__(self):
        self.outputs = 21
        
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.outputs, GPIO.OUT)
        GPIO.output(self.outputs, GPIO.LOW)

    def lightOutputs(self):
        for pin in self.outputs:
            GPIO.output(pin, GPIO.LOW)
        print("Lighting outputs...")
        for pin in self.outputs:
            print(f"Turning on output on pin {pin}")
            GPIO.output(pin, GPIO.LOW)
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
        # light.checkAllInputs()
    
if __name__ == "__main__":
    try:
        print("Initializing light system...")
        while True:
            print("starting in 5 seconds...")
            time.sleep(2) 
            print("starting 21")
            GPIO.output(21, GPIO.HIGH)
            time.sleep(2)
            print("turning off 21")
            GPIO.output(21, GPIO.LOW)
            time.sleep(2)
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    finally:
        GPIO.cleanup()

