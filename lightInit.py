import RPi.GPIO as GPIO

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
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    finally:
        GPIO.cleanup()



