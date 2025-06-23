from RPi.GPIO import GPIO

class Light:

    def __init__():
        outputs = [20, 21]
        # inputs = []
        GPIO.setmode(GPIO.BCM)

        for pin in outputs:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

        # for pin in inputs:
        #     GPIO.setup(pin, GPIO.IN)

    def setOutputs(self):
        for pin in self.outputs:
            GPIO.output(pin, GPIO.HIGH)

    def main():
        light = Light()
        light.setOutputs()
    
if __name__ == "__main__":
    Light.main()



