    


class Input:
    def __init__(self):
        self.order = [0, 1, 2, 3, 4, 5, 6]
        
        self.dicts = {
                0: [21, 19],
                1: [20, 13],
                2: [16, 6],
                3: [12, 5],
                4: [7, 9],
                5: [25, 27],
                6: [24, 18]
        }

    @staticmethod
    def entryInput(self):
        outputs = []
        inputs = []
        for num in self.order:
            outputs.append(self.dicts[num][0])
            inputs.append(self.dicts[num][1])

        return outputs, inputs
