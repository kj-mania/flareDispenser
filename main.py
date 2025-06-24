from light import Light
from flareSystem import flareSystem
import time as t

def main():
    outputs = [21, 20, 30, 40]
    inputs = [26, 19]

    light = Light(outputs, inputs)
    flareSystem = flareSystem()

    flareReturns = []

    for i in range(len(inputs)):
        outcome = flareSystem.fireFlare(i, light)
        flareReturns.append(outcome)
        t.sleep(3)
    
    allFlaresDeployed = flareSystem.flareSuccess(flareReturns)
    
    flareSystem.signalSuccess(allFlaresDeployed, light, 30, 40)



