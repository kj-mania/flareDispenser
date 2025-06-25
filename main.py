from light import Light
from flareSystem import FlareSystem
from inputManager import Order
from RPi import GPIO
import time as t

def run():
    order = Order()
    outputs, inputs, red, blue = order.entryInput()
    light = Light(outputs, inputs, red, blue)
    flareSystem = FlareSystem()

    flareReturns = []

    for i in range(len(inputs)):
        outcome = flareSystem.fireFlare(i, light)
        flareReturns.append(outcome)
        t.sleep(1)
    
    allFlaresDeployed = flareSystem.flareSuccess(flareReturns)
    print(f"All flares deployed successfully: {allFlaresDeployed}")
    print(flareReturns)
    flareSystem.signalSuccess(allFlaresDeployed, light, red, blue)

def main():
    try:
        while True:
            run()
            t.sleep(1)
            break
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()


#hi