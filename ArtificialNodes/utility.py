import numpy as np
import math
from constant import IDLE_RATIO

def getDistance(graph, start_node, end_node):
    if start_node in graph.node and end_node in graph.node:
        start_node = graph.node[start_node]
        end_node = graph.node[end_node]
        x_diff = start_node['X'] - end_node['X']
        y_diff = start_node['Y'] - end_node['Y']
        distance = pow((x_diff ** 2) * IDLE_RATIO + y_diff ** 2, 0.5)
        return distance
    else:
        return -1

def findAngle(graph, edge_pair, degrees=False):
    '''
    Finding the angle between the edge pair in the graph
    :param graph:  the graph information
    :param edge_pair: the edge pair
    :return: the angle in radians
    '''
    vectors = []
    for edge in edge_pair:

        point_1 = graph.node[edge[0]]
        point_2 = graph.node[edge[1]]

        # Computing the vector
        vector = {
            'X' : point_1['X'] - point_2['X'],
            'Y' : point_1['Y'] - point_2['Y'],
        }

        # Appending the vector
        vectors.append((vector['X'], vector['Y']))

    angle_rad = angle_between(vectors)

    if degrees:
        return math.degrees(angle_rad)
    return angle_rad

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(vector_pair):
    '''
    Returns the angle in radians between the pair of two vectors ::
    :param vector_pair:
    :return: Angle in radians
    '''
    v1_u = unit_vector(vector_pair[0])
    v2_u = unit_vector(vector_pair[1])
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

