from light import Light
from flareSystem import FlareSystem
import time as t

outputs = [21, 20]
inputs = [19, 13]
light = Light(outputs, inputs)

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

    # flareSystem.signalSuccess(allFlaresDeployed, light, 30, 40)

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