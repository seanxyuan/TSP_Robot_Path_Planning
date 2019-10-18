import networkx as nx
from collections import Counter
import utility

class BasicGraph(object):
    def __init__(self, data):
        self.data = data

    def createBasicGraph(self):
        '''
        Creating a basic graph, if data about the graph exists.
        '''
        self.graph = None
        # If graph data exists
        if self.data:
            self.graph = nx.Graph()

            nodes = self.data['nodes']
            edges = self.data['edges']

            for node in nodes:
                self.graph.add_node(node['id'], X = node['X'], Y = node['Y'])

            for edge in edges:
                self.graph.add_edge(edge['start'], edge['end'], DEPOSITION_EDGE = True)

    def getOtherNodes(self, node):
        '''
        Get all nodes other than the current node
        :param node: the current node's ID
        :return: a list of nodes other than the current node
        '''
        node_list = []
        for node_object in self.graph.node:
            if node != node_object:
                node_list.append(node_object)

        return node_list

    def addIdleEdges(self):
        '''
        Adding Idle edges to the graph
        '''
        for start_node, edges in self.graph.edge.iteritems():
            other_nodes = Counter(self.getOtherNodes(start_node))
            adjacent_nodes = []
            for end_node, weight in edges.iteritems():
                adjacent_nodes.append(end_node)
            adjacent_nodes = Counter(adjacent_nodes)

            missing_nodes = other_nodes - adjacent_nodes

            for node in missing_nodes:
                weight = utility.getDistance(self.graph, start_node, end_node)
                self.graph.add_edge(start_node, node, weight = weight, IDLE_EDGES = True)
            pass