from light import Light
from flareSystem import FlareSystem
from inputManager import Order
from RPi import GPIO
import time as t

# outputs = [21, 20, 16, 12, 7, 25, 24]
# inputs = [19, 13, 6, 5, 9, 27, 18]


# light = Light(outputs, inputs, red, blue)



def run():
    red = 17
    blue = 15
    order = Order()
    outputs, inputs = order.entryInput()
    light = Light(outputs, inputs, red, blue)
    flareSystem = FlareSystem()

    flareReturns = []

    for i in range(len(inputs)):
        outcome = flareSystem.fireFlare(i, light)
        flareReturns.append(outcome)
        t.sleep(3)
    
    allFlaresDeployed = flareSystem.flareSuccess(flareReturns)
    print(f"All flares deployed successfully: {allFlaresDeployed}")
    print(flareReturns)
    flareSystem.signalSuccess(allFlaresDeployed, light, red, blue)

    return light

def main():
    try:
        while True:
            run()
            t.sleep(1)
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()


#hi