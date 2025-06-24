import time
from typing import List
from light import Light

class FlareSystem:

    def __init__(self):
        self.delay = 3

    def flareSuccess(self, outcomes: list[bool]) -> bool:
        sum = 0
        for outcome in outcomes:
            if outcome:
                success += 1
        return success == len(outcomes)
    
    def fireFlare(self, index: int, light: Light) -> bool:
        flareOut = light.outputs[index]
        flareToReturn = light.inputs[index]
        light.activate(flareOut)
        return light.inputOn(flareToReturn)
    
    def signalSuccess(self, success: bool, light: Light, red: int, green: int):
        if success:
            light.activate(green)
        else:
            light.activate(red)

    

    

    






    


    