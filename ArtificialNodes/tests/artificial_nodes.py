import unittest
from ArtificialNodes import input, basic_graph, add_nodes

class CheckNodesAdded(unittest.TestCase):
    '''
    Checking if the count of artificial nodes added is equal to the number of edges in the original graph.
    '''
    def test_nodes_added(self):
        """Is five successfully determined to be prime?"""
        graphInput = input.Input()
        graphInput.readFile('input.json')

        # Construction the graph from the input
        graph = basic_graph.BasicGraph(graphInput.data)
        graph.createBasicGraph()

        original_edges = graph.graph.number_of_edges()
        # Adding the extra nodes in the graph depending upon the degree of the node.
        extra_nodes = add_nodes.AddingNodes(graph)
        extra_nodes.addNodes()

        nodes_after_addition = graph.graph.number_of_nodes()

        condition = True if original_edges * 2 == nodes_after_addition  else False
        self.assertTrue(condition)

if __name__ == '__main__':
    unittest.main()