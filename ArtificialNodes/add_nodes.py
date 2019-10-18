import itertools, utility
from constant import ROTATION_COST

class AddingNodes(object):
    def __init__(self, input):
        self.data = input.data
        self.graph = input.graph

    def findNodes(self):
        '''
        Finding the nodes to be added.
        :return: the list of nodes that needs to be added in the graph
        '''
        extra_node_list = []

        # If graph data exists
        if self.graph:

            for node, edges in self.graph.edge.iteritems():
                edge_count = len(edges)
                node_info = self.graph.node[node]
                if edge_count > 1:
                    for index in range(1, edge_count):
                        extra_node = str(node) + '_' + str(index)

                        edge_pair = []
                        for node_pair in itertools.product(node, edges):
                            edge_pair.append(node_pair)

                        rotation_angle = utility.findAngle(self.graph, edge_pair, degrees=True)

                        node_object = {
                                'id': extra_node,
                                'X' : node_info['X'],
                                'Y' : node_info['Y'],
                                'angle': rotation_angle
                            }
                        extra_node_list.append(node_object)
        return extra_node_list

    def addNodes(self):
        '''
        Addition of extra nodes
        :return:
        '''

        for node in self.findNodes():
            node_id = node['id']
            node_x = node['X']
            node_y = node['Y']
            self.graph.add_node(node_id, X = node_x, Y = node_y)
            self.addRotationCost(node)

        # Added all the artificial nodes
        # Now, adding all the idle edges to make a complete graph.
        self.addIdleEdges()

    def addRotationCost(self, artificial_node):
        '''
        Adding the rotation cost for the newly added node
        :param artificial_node: the added node
        :return:
        '''
        node_id = artificial_node['id']
        index = node_id.index('_')
        original_node = node_id[:index]
        rotation_cost = artificial_node['angle'] * ROTATION_COST
        self.graph.add_edge(original_node, node_id, ROTATION_COST = rotation_cost)

    def addIdleEdges(self):
        '''
        Adding idle edges to make the graph fully complete
        :return:
        '''
        nodes = self.graph.node

        for start_node, start_info in nodes.iteritems():
            for end_node, end_info in nodes.iteritems():
                if start_node != end_node and not self.graph.has_edge(start_node, end_node):
                    distance = utility.getDistance(self.graph, start_node, end_node)
                    self.graph.add_edge(start_node, end_node, IDLE_COST = distance)