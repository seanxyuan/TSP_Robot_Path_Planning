import input, basic_graph, add_nodes, deposition_cost

class ArtiticialNodes(object):
    def __init__(self):
        pass

    def readFile(self):
        # Reading the graph from the input file
        self.graphInput = input.Input()
        self.graphInput.readFile('input.json')

    def makeGraph(self):
        # Construction the graph from the input
        self.graph = basic_graph.BasicGraph(self.graphInput.data)
        self.graph.createBasicGraph()

    def addAdditionalNodes(self):
        # Adding the extra nodes in the graph depending upon the degree of the node.
        self.graph = add_nodes.AddingNodes(self.graph)
        self.graph.addNodes()

    def addDepositionCost(self):
         # Assigning the deposition costs
        self.graph = deposition_cost.DepositionCost(self.graph)
        self.graph.assignDepositionCost()

    def main(self):
        self.readFile()
        self.makeGraph()
        self.addAdditionalNodes()
        self.addDepositionCost()
        return self.graph