from constant import DEPOSITION_RATIO

class DepositionCost(object):
    '''
    This class would be computing the depostion cost for the deposition edges
    and would then assign them to the deposition edges.

    The deposition cost would be computed using the 5 times than maximum IDLE time in the graph.
    '''

    def __init__(self, graph):
        self.graph = graph.graph

    def computeMaxRotationCost(self):
        '''
        :return: Retuning the the maximum rotation cost.
        '''
        max_rotation_cost = 0
        idle_edges = self.getEdgeByKey('ROTATION_COST')

        for edge in idle_edges:
            data = edge[2]
            cost = data['ROTATION_COST']
            if cost > max_rotation_cost:
                max_rotation_cost = cost
        return max_rotation_cost

    def computeMaxIdleCost(self):
        '''
        :return: Retuning the the maximum idle edge cost.
        '''
        max_idle_cost = 0
        idle_edges = self.getEdgeByKey('IDLE_COST')

        for edge in idle_edges:
            data = edge[2]
            cost = data['IDLE_COST']
            if cost > max_idle_cost:
                max_idle_cost = cost
        return max_idle_cost


    def comptuteDepositionCost(self):
        '''
        :return: Retuning the the deposition cost
        '''
        idle_cost  = self.computeMaxIdleCost()
        rotation_cost = self.computeMaxRotationCost()

        deposition_cost = DEPOSITION_RATIO * (idle_cost + rotation_cost)

        return deposition_cost

    def getEdgeByKey(self, key):
        '''
        Returning the list of edges based of the key presence
        :param key: the key that would be searched in the edge's data
        :return: a list of edges that contain the key
        '''
        edge_list = []

        for edge in self.graph.edges(data=True):
            data = edge[2]
            if key in data:
                edge_list.append(edge)

        return edge_list

    def assignDepositionCost(self):
        '''
        Assigning the deposition cost to the edges
        :return:
        '''
        deposition_cost = self.comptuteDepositionCost()
        # edges = self.graph.edges_iter(data='DEPOSITION_EDGE',default=1)
        edges = self.graph.edges(data=True)

        # Getting all the deposition edges
        deposition_edges = self.getEdgeByKey('DEPOSITION_EDGE')

        total_deposition_cost = 0

        # Assigning the deposition edges the required deposition cost
        for deposition_edge in deposition_edges:
            data = deposition_edge[2]
            data['DEPOSITION_COST'] = deposition_cost
            total_deposition_cost += deposition_cost

        self.total_deposition_cost = total_deposition_cost

