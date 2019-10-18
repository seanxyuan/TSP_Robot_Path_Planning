from ortools.constraint_solver import pywrapcp
from input import Input
from util import get_edge_type_cost
from constant import EDGE_TPYE
from ArtificialNodes.utility import getDistance

class TSP(object):
    def __init__(self, graph):
        '''
        Initializing the TSP object
        :param graph: the input graph with artificial nodes already added
        '''
        self.tsp_use_random_matrix = True
        self.use_light_propagation = False
        self.graph = graph.graph
        self.total_deposition_cost = graph.total_deposition_cost

    def setup(self, size):
        '''
        Configuration of the TSP module
        :param size: the size of the matrix
        '''
        param = pywrapcp.RoutingParameters()
        param.use_light_propagation = self.use_light_propagation
        pywrapcp.RoutingModel.SetGlobalParameters(param)

        # TSP of size FLAGS.tsp_size
        # Second argument = 1 to build a single tour (it's a TSP).
        # Nodes are indexed from 0 to FLAGS_tsp_size - 1, by default the start of
        # the route is node 0.
        self.routing = pywrapcp.RoutingModel(size, 1)

        self.parameters = pywrapcp.RoutingSearchParameters()

        # Setting first solution heuristic (cheapest addition).
        self.parameters.first_solution = 'PathCheapestArc'

        # Disabling Large Neighborhood Search, comment out to activate it.
        self.parameters.no_lns = True
        self.parameters.no_tsp = False

    def run(self):
        '''
        The actual execution method solving the TSP problem
        :return: the solution of the TSP problem
        '''
        matrix = Input(self.graph)
        matrix.transform()

        self.setup(matrix.getSize())

        # Setting the cost function.
        # Put a callback to the distance accessor here. The callback takes two
        # arguments (the from and to node inidices) and returns the distance between
        # these nodes.

        node_alias = matrix.node_alias

        matrix_callback = matrix.Distance
        if self.tsp_use_random_matrix:
            self.routing.SetArcCostEvaluatorOfAllVehicles(matrix_callback)
        else:
            self.routing.SetArcCostEvaluatorOfAllVehicles(self.Distance)

        return self.getSolution(node_alias, self.solve())

    def getSolution(self, node_alias, solution):
        '''
        Getting the final solution in terms of node labels.
        :param node_alias: the map having node and their aliases
        :param solution: the final solution with node indexes
        :return: the final solution dictionary
        '''
        node_mapping = {v: k for k, v in node_alias.items()}
        node_route = []

        for node in solution['nodes']:
            node_route.append(node_mapping[node])

        solution['nodes'] = node_route
        solution['cost'] = self.compute_tsp_cost(node_route)
        return solution

    def compute_tsp_cost(self, route):
        '''
        Computing the cost of the solution. Currently focusing on the idle cost.
        :param route: the final TSP route
        :return: the idle cost
        '''
        idle_cost = 0
        rotation_cost = 0
        deposition_cost = 0

        for node_index in range(1, len(route)):
            start_node = route[node_index - 1]
            end_node = route[node_index]
            edge_data = self.graph.edge[start_node][end_node]

            cost = get_edge_type_cost(edge_data)

            if cost['type'] != EDGE_TPYE.DEPOSITION:
                if cost['type'] == EDGE_TPYE.ROTATION:
                    rotation_cost += cost['cost']
                else:
                    idle_cost += cost['cost']
            else:
                cost = getDistance(self.graph, start_node, end_node)
                deposition_cost += cost
        return {
            'idle': idle_cost,
            'rotation': rotation_cost,
            'deposition': deposition_cost
        }

    def solve(self):
        '''
        Solving the TSP problem
        :return: the solution object
        '''
        solution = {}
        # Solve, returns a solution if any.
        assignment = self.routing.SolveWithParameters(self.parameters, None)
        if assignment:
            # Solution cost.
            print 'Final Cost is ', assignment.ObjectiveValue()
            solution['cost'] = assignment.ObjectiveValue()
            # Inspect solution.
            # Only one route here; otherwise iterate from 0 to routing.vehicles() - 1
            route_number = 0
            node = self.routing.Start(route_number)
            route = ''

            print '\n\nThe solution is the following: '
            while not self.routing.IsEnd(node):
                route += str(node) + ' -> '
                node = assignment.Value(self.routing.NextVar(node))
                print 'Route : ', route
            else:
                route += '0'
                print '\n\nFinal Route is ', route

                routeNodes = route.split(' -> ')
                nodes = []
                for node in routeNodes:
                    nodes.append(int(node))
                solution['nodes'] = nodes
        else:
            print 'Specify an instance greater than 0.'
        return solution

if __name__ == '__main__':
    solution = TSP().run()
    print solution