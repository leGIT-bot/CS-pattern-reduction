import random

def GenerateDynamicTable(sizes, stripSize):
    DynamicTable = [0]*(stripSize + 1)
    for i in range(0, stripSize + 1):
        DynamicTable[i] = {'currentSolution':[], 'remainingSizes':[], 'previousSolutions':[]}

    DynamicTable[0]['remainingSizes'] = DetermineAvailableSizes(stripSize, sizes)

    ReturnChild(DynamicTable)
    #for i in range(0, stripSize + 1):
    #    if len(DynamicTable[i]['remainingSizes']) > 0:
    #        size = DynamicTable[i]['remainingSizes'].pop()
    #        DynamicTable[i + size]['previousSolutions'].append(DynamicTable[i]['currentSolution'] + [size])
    #        DynamicTable[i + size]['currentSolution'] = DynamicTable[i]['currentSolution'] + [size]
    #        DynamicTable[i + size]['remainingSizes'] = DetermineAvailableSizes(stripSize - i - size, DynamicTable[i]['remainingSizes'])
    #
    #if DynamicTable[stripSize]['currentSolution'] == []:
    #    DynamicTable[stripSize]['currentSolution'] = None

    return DynamicTable

def DetermineAvailableSizes(spaceLeft, sizes):
    AvailableSizes = []
    if isinstance(sizes, list):
        for size in sizes:
            if size <= spaceLeft:
                AvailableSizes.append(size)
    else:
        for size in sizes:
            if size <= spaceLeft:
                for _ in range(0, sizes[size]):
                    AvailableSizes.append(size)
    return AvailableSizes


def ReturnChild(DynamicTable):
    TableLength = len(DynamicTable) - 1
    returnSolution = DynamicTable[TableLength]['currentSolution']

    NewSolutionFound = False
    backtracking = True
    CurrentPosition = TableLength - 1
    while NewSolutionFound == False:
        if backtracking:
            if len(DynamicTable[CurrentPosition]['remainingSizes']) > 0:
                size = DynamicTable[CurrentPosition]['remainingSizes'].pop()
                newSolution = DynamicTable[CurrentPosition]['currentSolution'] + [size]
                if CheckRepeatSolution(newSolution, DynamicTable[CurrentPosition + size]['previousSolutions']):
                    DynamicTable[CurrentPosition + size]['previousSolutions'].append(newSolution)
                    DynamicTable[CurrentPosition + size]['currentSolution'] = newSolution
                    DynamicTable[CurrentPosition + size]['remainingSizes'] = DetermineAvailableSizes(TableLength - CurrentPosition - size, DynamicTable[CurrentPosition]['remainingSizes'])
                    backtracking = False
                    CurrentPosition = CurrentPosition + size
            else:
                CurrentPosition = CurrentPosition - 1
        else:
            if CurrentPosition == TableLength:
                #print(DynamicTable[TableLength]['previousSolutions'])
                NewSolutionFound = True
            else:
                if len(DynamicTable[CurrentPosition]['remainingSizes']) > 0:
                    size = DynamicTable[CurrentPosition]['remainingSizes'].pop()
                    newSolution = DynamicTable[CurrentPosition]['currentSolution'] + [size]
                    if CheckRepeatSolution(newSolution, DynamicTable[CurrentPosition + size]['previousSolutions']):
                        DynamicTable[CurrentPosition + size]['previousSolutions'].append(newSolution)
                        DynamicTable[CurrentPosition + size]['currentSolution'] = DynamicTable[CurrentPosition]['currentSolution'] + [size]
                        DynamicTable[CurrentPosition + size]['remainingSizes'] = DetermineAvailableSizes(TableLength - CurrentPosition - size, DynamicTable[CurrentPosition]['remainingSizes'])
                        CurrentPosition = CurrentPosition + size
                else:
                    backtracking = True
                    CurrentPosition = CurrentPosition - 1

        if CurrentPosition < 0:
            NewSolutionFound = True
            DynamicTable[TableLength]['currentSolution'] = None

    return returnSolution


def CheckRepeatSolution(newSolution, Solutions):
    for solution in Solutions:
        i = 0
        if len(solution) == len(newSolution):
            while solution[i] == newSolution[i]:
                if i + 2 > len(solution):
                    return False
                else:
                    i = i + 1
    return True

def RemoveRepeatedLists(Lists):
    ReturnLists = []
    i = 0
    while i < len(Lists):
        Lists[i].sort()
        repeat = 0
        j = 0
        while j < len(ReturnLists) and repeat == 0:
            k = 0
            identical = 1
            while k < len(Lists[i]) and identical == 1:
                if ReturnLists[j][k] != Lists[i][k]:
                    identical = 0
                k += 1

            if identical == 1:
                repeat = 1
            j += 1

        if repeat == 0:
            ReturnLists.append(Lists[i])

        i += 1

    return ReturnLists
#print(DynamicCuttingStock([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5], 10))
#print(DynamicCuttingStock({138:22, 152:25, 156:12, 171:14, 182:18, 188:18, 193:20, 200:10, 205:12, 210:14, 214:16, 215:18, 220:20}, 560))