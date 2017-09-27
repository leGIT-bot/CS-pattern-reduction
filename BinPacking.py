import math

def BinPacking(sizes, stripSize, isStrips):
    Strips = [[]]
    SortedSizes = []
    if isStrips:
        SortedSizes = FindSortedSizesFromStrips(sizes)
    else:
        SortedSizes = FindSortedSizesFromSizes(sizes)

    while len(SortedSizes) > 0:
        size = SortedSizes.pop()
        i = 0
        spotFound = False
        while not spotFound:
            if StripTotalSize(Strips[i]) + size <= stripSize:
                Strips[i].append(size)
                spotFound = True
            i += 1
            if i == len(Strips) and not spotFound:
                Strips.append([])
    return(ProcessStripsIntoDictionary(Strips))

def StripTotalSize(Strip):
    Size = 0
    for i in Strip:
        Size += i
    return Size

def FindSortedSizesFromStrips(sizes):
    ReturnSizes = []
    for strip in sizes:
        for size in sizes[strip]['strip']:
            BinaryInsert(ReturnSizes, size, sizes[strip]['amount'])
    return ReturnSizes

def FindSortedSizesFromSizes(sizes):
    ReturnSizes = []
    for size in sizes:
        BinaryInsert(ReturnSizes, size, sizes[size])
    return ReturnSizes

def BinaryInsert(Sizes, size, amount):
    start = 0
    end = len(Sizes) - 1
    while start <= end:
        center = math.ceil((start+end)/2)
        if Sizes[center] == size:
            for _ in range(0, amount):
                Sizes.insert(center, size)
            print(Sizes)
            return
        elif size < Sizes[center]:
            end = center - 1
        else:
            start = center + 1
    center = math.ceil(start+end/2)
    if center > end:
        for _ in range(0, amount):
            Sizes.append(size)
    else:
        for _ in range(0, amount):
            Sizes.insert(center, size)

def ProcessStripsIntoDictionary(sizes):
    returnDictionary = {}
    for i in sizes:
        try:
            returnDictionary[str(i)]['amount'] += 1
        except KeyError:
            returnDictionary[str(i)] = {'amount':1, 'strip':i}
    return returnDictionary

if __name__ == "__main__":
    Sizes = {2:15, 3:10, 5:8}
    print(BinPacking(Sizes, 10, False))