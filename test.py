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
        while True:
            for pin in self.outputs:
                print(f"Turning on output on pin {pin}")
                GPIO.output(pin, GPIO.HIGH)
                time.sleep(5)

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

