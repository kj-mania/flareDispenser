from light import Light
from flareSystem import FlareSystem
import time as t

def run():
    outputs = [21, 20, 30, 40]
    inputs = [26, 19]

    light = Light(outputs, inputs)
    flareSystem = FlareSystem()

    flareReturns = []

    for i in range(len(inputs)):
        outcome = flareSystem.fireFlare(i, light)
        flareReturns.append(outcome)
        t.sleep(3)
    
    allFlaresDeployed = flareSystem.flareSuccess(flareReturns)
    
    flareSystem.signalSuccess(allFlaresDeployed, light, 30, 40)


def main():
    try:
        while True:
            run()
            t.sleep(1)
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    finally:
        Light.cleanup()



