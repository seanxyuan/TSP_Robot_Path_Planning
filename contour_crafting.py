from ArtificialNodes import artificial_nodes
from TSP.TSP import TSP

class ContourCrafting(object):
    def __init__(self):
        pass

    def run(self):
        '''
        Solving the Contour Crafting problem
        :return:
        '''
        nodes = artificial_nodes.ArtiticialNodes()
        graph = nodes.main()

        TSP_object = TSP(graph)
        self.solution = TSP_object.run()

    def get_solution(self):
        return self.solution