from seed_class import seed
from DynamicProgrammingAlgorithm import DynamicCuttingStock

class CuttingStockProblem():
    def __init__(self, Solution, StripSize):
        self.StripSize = StripSize
        self.BaseNode = seed(Solution, None, None, 0, StripSize)
        self.Nodes = [self.BaseNode]
        self.NodesToExamineStack = [self.BaseNode]

        self.BestSolution = Solution
        self.BestWaste = self.CalculateWaste(Solution)
        self.BestStrips = self.CalculateStrips(Solution)
        self.PrintCurrentSolution()

        self.SolveCuttingStock()

    def SolveCuttingStock(self):
        Halt = False
        while not Halt:
            while len(self.NodesToExamineStack) > 0:
                # print(NodesToExamineStack[len(NodesToExamineStack) - 1].bins)
                self.ExamineNode(self.NodesToExamineStack.pop(len(self.NodesToExamineStack) - 1))
            for node in self.Nodes:
                self.ExamineNode(node)
            if len(self.NodesToExamineStack) == 0:
                Halt = True

        self.PrintCurrentSolution()
        print('FINAL SOLUTION')

    def ExamineNode(self, Node):
        for i in range(10):
            # print('Tableb: ' + str(Node.table))
            NewNode = Node.getChild()
            if NewNode is not None:
                if not self.IgnoreNewNode(NewNode):
                    self.Nodes.append(NewNode)
                    self.NodesToExamineStack.append(NewNode)
                else:
                    i -= 1
            else:
                if i == 0:
                    Solution = self.CompileSolution(Node)
                    #print('Solution: ' + str(Solution))
                    #print('Waste: ' + str(100*self.CalculateWaste(Solution)) + '%')
                    #print('Strips: ' + str(self.CalculateStrips(Solution)))
                    #print('----------')
                    if self.UpdateSolution(Solution):
                        self.PrintCurrentSolution()
                break

    def IgnoreNewNode(self, NewNode):
        NodeSeed = NewNode.structure
        Parent = NewNode.parent

        while Parent is not None:
            if NodeSeed == Parent.structure:
                return True
            else:
                Parent = Parent.parent

        Solution = self.CompileSolution(NewNode)
        if self.CalculateStrips(Solution) > self.BestStrips:
            return True

        return False

    def UpdateSolution(self, Solution):
        newWaste = self.CalculateWaste(Solution)
        newStrips = self.CalculateStrips(Solution)

        if newStrips < self.BestStrips:
            self.BestSolution = Solution
            self.BestWaste = newWaste
            self.BestStrips = newStrips
            return True
        elif newStrips == self.BestStrips:
            if newWaste < self.BestWaste:
                self.BestSolution = Solution
                self.BestWaste = newWaste
                self.BestStrips = newStrips
                return True
        print('Solution: ' + str(Solution))
        print('Waste: ' + str(100 * newWaste) + '%')
        print('MasterStrips: ' + str(newStrips))
        print('---------- Solution rejected')
        return False

    def PrintCurrentSolution(self):
        print('Solution: ' + str(self.BestSolution))
        print('Waste: ' + str(100 * self.BestWaste) + '%')
        print('MasterStrips: ' + str(self.BestStrips))
        print('---------- Best solution')

    def CalculateWaste(self, Solution):
        totalUse = 0
        nStrips = 0
        for strip in Solution:
            nStrips += Solution[strip]['amount']
            for size in Solution[strip]['strip']:
                totalUse += size*Solution[strip]['amount']
        return 1 - totalUse/(nStrips*self.StripSize)

    def CalculateStrips(self, Solution):
        nStrips = 0
        for strip in Solution:
            nStrips += 1

        return nStrips

    def CompileSolution(self, Node):
        Solution = Node.bins
        while Node.parent is not None:
            try:
                Solution[str(Node.structure)]['amount'] += Node.amount
            except KeyError:
                Solution[str(Node.structure)] = {'amount': Node.amount, 'strip': Node.structure}
            Node = Node.parent
        return Solution

if __name__ == '__main__':
    StripSize = 560
    Sizes = {138:22, 152:25, 156:12, 171:14, 182:18, 188:18, 193:20, 200:10, 205:12, 210:14, 214:16, 215:18, 220:20}
    #StripSize = 10
    #Sizes = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]
    #StripSize = 10
    #Sizes = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5]

    Sizes = DynamicCuttingStock(Sizes, StripSize)

    CuttingStockProblem(Sizes, StripSize)