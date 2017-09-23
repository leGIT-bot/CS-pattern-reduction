import random
from DynamicProgrammingAlgorithm import DynamicCuttingStock

from ReturnSeeds import GenerateDynamicTable
from ReturnSeeds import ReturnChild

class seed():
    def __init__(self, bulk, structure, parent, amount, stripSize):
        self.bins = bulk
        self.children = []
        self.structure = structure
        self.parent = parent
        self.amount = amount
        self.stripSize = stripSize
        self.seedAmount = GreatestSize(bulk)
        Subset = FindSubsetFromStrips(bulk, self.seedAmount)
        self.table = GenerateDynamicTable(Subset, stripSize)

    def getChild(self):
        while self.seedAmount > 1:
            NewSeed = ReturnChild(self.table)
            if NewSeed is not None:
                newBulk = FindBulk(self.bins, NewSeed, self.seedAmount, self.stripSize)
                return seed(newBulk, NewSeed, self, self.seedAmount, self.stripSize)
            else:
                Subset = FindSubsetFromStrips(self.bins, self.seedAmount)
                self.table = GenerateDynamicTable(Subset, self.stripSize)
                self.seedAmount -= 1
                print(str(Subset) + ': ' + str(self.seedAmount))
        return None

def GreatestSize(strips):
    sizes = FindSubsetFromStrips(strips, 1)
    LargestSize = 0
    for i in sizes:
        if sizes[i] > LargestSize:
            LargestSize = sizes[i]
    return LargestSize

def FindBulk(bulk, seed, amount, stripSize):
    BulkSizes = BulkToSizes(bulk)
    for i in seed:
        BulkSizes[i] -= amount

    BulkSizes = DynamicCuttingStock(BulkSizes, stripSize)
    return BulkSizes

def FindSubsetFromStrips(strips, subset):
    returnSizes = {}
    for strip in strips:
         for i in strips[strip]['strip']:
            try:
                returnSizes[i] += strips[strip]['amount']
            except KeyError:
                returnSizes[i] = strips[strip]['amount']

    RemoveSizes = []
    for number in returnSizes:
        returnSizes[number] = (returnSizes[number] + 1)//subset
        if returnSizes[number] == 0:
            RemoveSizes.append(number)

    for i in RemoveSizes:
        del returnSizes[i]

    return returnSizes

def BulkToSizes(bulk):
    Sizes = {}
    for strip in bulk:
        for size in bulk[strip]['strip']:
            try:
                Sizes[size] += bulk[strip]['amount']
            except KeyError:
                Sizes[size] = bulk[strip]['amount']
    return Sizes


def ProcessSizesIntoDictionary(sizes):
    returnDictionary = {}
    for i in sizes:
        try:
            returnDictionary[i] += 1
        except KeyError:
            returnDictionary[i] = 1
    return returnDictionary

def bulk_to_array(bulk):
    output = []
    for key in bulk:
        output += bulk[key]*key
    return output

if __name__ == "__main__":
    StripSize = 10
    Sizes = DynamicCuttingStock([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5], StripSize)

    BaseNode = seed(Sizes, None, None, 0, StripSize)
    NewNode = BaseNode.getChild()