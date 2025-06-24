from light import Light
from flareSystem import FlareSystem
import time as t

def run() -> Light:
    outputs = [21, 20]
    inputs = [19, 13]

    light = Light(outputs, inputs)
    flareSystem = FlareSystem()

    flareReturns = []

    for i in range(len(inputs)):
        outcome = flareSystem.fireFlare(i, light)
        flareReturns.append(outcome)
        t.sleep(3)
    
    allFlaresDeployed = flareSystem.flareSuccess(flareReturns)
    print(f"All flares deployed successfully: {allFlaresDeployed}")

    return light
    # flareSystem.signalSuccess(allFlaresDeployed, light, 30, 40)

def main():
    try:
        while True:
            light = run()
            t.sleep(1)
    except KeyboardInterrupt:
        print("Program interrupted by user.")
        light.cleanup()
    finally:
        light.cleanup() 

if __name__ == "__main__":
    main()


#hi