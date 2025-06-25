from light import Light
from flareSystem import FlareSystem
import time as t

outputs = [21, 20, 16, 12, 7, 25, 24]
inputs = [19, 13, 6, 5, 9, 27, 18]
red = 17
blue = 15
light = Light(outputs, inputs, red, blue)

def run():
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

def main():
    try:
        while True:
            run()
            t.sleep(1)
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    finally:
        light.cleanup() 

if __name__ == "__main__":
    main()


#hi