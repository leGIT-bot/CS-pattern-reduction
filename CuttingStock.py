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
            if not IgnoreNewNode(NewNode):
                Nodes.append(NewNode)
                NodeStack.append(NewNode)
            else:
                i -= 1
        else:
            if i == 0:
                #print('Tablea: ' + str(Node.table))
                print('Bins: ' + str(Node.bins))
                print('Seeds: ' + str(CompileSolution(Node)))
                print('----------')
            break

def IgnoreNewNode(NewNode):
    NodeSeed = NewNode.structure
    Parent = NewNode.parent

    while Parent is not None:
        if NodeSeed == Parent.structure:
            return True
        else:
            Parent = Parent.parent
    return False

def CompileSolution(Node):
    Solution = {}
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
    Sizes = DynamicCuttingStock(Sizes, StripSize)

    SolveCuttingStock(Sizes, StripSize)