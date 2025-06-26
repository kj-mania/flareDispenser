import time
from typing import List
from light import Light

class FlareSystem:

    def __init__(self):
        self.delay = 1

    def flareSuccess(self, outcomes: list[bool]) -> bool:
        success = 0
        for outcome in outcomes:
            if outcome:
                success += 1
        return success == len(outcomes)
    
    def fireFlare(self, index: int, light: Light) -> bool:
        flareOut = light.outputs[index]
        flareToReturn = light.inputs[index]
        light.activate(flareOut)
        time.sleep(.5)
        return light.inputOn(flareToReturn)
    
    def printFailure(self, failures: list[int]):
        for idx, item in reversed(list(enumerate(failures))):
            if item == 0:
                print(f"Flare {idx} failed to deploy")
    
    def signalSuccess(self, success: bool, light: Light, red: int, blue: int):
        if success:
            print("Activating blue light to signal success.")
            light.activate(blue)
            light.deactivate(red)

        else:
            print("Activating red light to signal failure.")
            light.deactivate(blue)
            for _ in range(20):
                light.activate(red)
                time.sleep(.1)
                light.deactivate(red)
                time.sleep(.1)
