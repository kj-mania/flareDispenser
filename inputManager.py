class Order:
    def __init__(self):

        self.order = self.getOrder()
        
        self.red = 17
        self.blue = 15

        self.dicts = {
                0: [21, 19],
                1: [20, 13],
                2: [16, 6],
                3: [12, 5],
                4: [7, 9],
                5: [25, 27],
                6: [24, 18]
        }

        self.enterCode = 7

    def entryInput(self):
        outputs = []
        inputs = []
        for num in self.order:
            outputs.append(self.dicts[num][0])
            inputs.append(self.dicts[num][1])

        return outputs, inputs, self.red, self.blue
    
    def getOrder(self):
        newOrder = []
        for i in range (7):
            x = input("Input order one at a time:")
            if int(x) == 7:
                newOrder = [0, 1, 2, 3, 4, 5, 6]
                break
            newOrder.append(int(x))
            
        return newOrder
            