import RPi.GPIO as GPIO
import time

class Light:
    def __init__(self):
        self.outputs = [21, 20]
        
        GPIO.setmode(GPIO.BCM)

        for pin in self.outputs:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

    def lightOutputs(self):
        print("Lighting outputs 21")
        GPIO.output(21, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(21, GPIO.LOW)
        print("Lighting outputs 20")
        GPIO.output(20, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(20, GPIO.LOW)

    @staticmethod
    def main():
        light = Light()
        light.lightOutputs()
    
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

