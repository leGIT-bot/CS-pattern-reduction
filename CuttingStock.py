from seed_class import seed
from DynamicProgrammingAlgorithm import DynamicCuttingStock

def SolveCuttingStock(Solution, StripSize):
    BaseNode = seed(Sizes, None, None, 0, StripSize)
    Nodes = []
    NodesToExamineStack = [BaseNode]

    while len(NodesToExamineStack) > 0:
        #print(NodesToExamineStack[len(NodesToExamineStack) - 1].bins)
        ExamineNode(NodesToExamineStack.pop(len(NodesToExamineStack) - 1), Nodes, NodesToExamineStack)

def ExamineNode(Node, Nodes, NodeStack):
    for i in range(10):
        #print('Tableb: ' + str(Node.table))
        NewNode = Node.getChild()
        if NewNode is not None:
            Nodes.append(NewNode)
            NodeStack.append(NewNode)
        else:
            if i == 0:
                #print('Tablea: ' + str(Node.table))
                print('Bins: ' + str(Node.bins))
                print('Seeds: ' + str(CompileSolution(Node)))
                print('----------')
            break

def CompileSolution(Node):
    Solution = {}
    while Node.parent is not None:
        Solution[str(Node.structure)] = {'amount':Node.amount, 'strip':Node.structure}
        Node = Node.parent
    return Solution

if __name__ == '__main__':
    StripSize = 10
    Sizes = DynamicCuttingStock([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5], StripSize)

    SolveCuttingStock(Sizes, StripSize)