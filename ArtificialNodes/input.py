import networkx as nx
from  constant import DEPOSITION_RATIO
import os
import json

class Input(object):
    def __init__(self, type = 'json'):
        '''
        Creating the input class
        :param type: the type of input, currently defaults to JSON
        '''
        self.type = type
        self.directory = os.path.dirname(os.path.abspath(__file__))

    def setFileName(self, filename):
        '''
        Setting the filename for the input if the file exists, otherwise setting to None.
        :param filename: the filename of the input file
        '''
        data_location = os.path.join(self.directory, 'data')

        # Data location exists
        if os.path.exists(data_location):
            file_location = os.path.join(data_location, filename)

            # File location exists
            if os.path.exists(file_location):
                self.file_location = file_location
            else:
                self.file_location = None

    def readFile(self, filename):
        '''
        Reading from the file, if the file actually exists
        :param filename: the filename for the input
        '''
        self.setFileName(filename)

        # Initialize data to None
        self.data = None

        # If the file exists
        if self.file_location:
            with open(self.file_location) as data_file:
                data = json.load(data_file)

                self.data = data



    def parseGraph(self):
        '''
        This method would read the input from a file.
        The input would be in the form of (x,y) for every node
        '''

        nodes = {}
        edges = []

        for index in range(2):
            nodes['A'+str(index)] = {
                'x': 0,
                'y': 0
            }
            nodes['B'+str(index)] = {
                'x': 0,
                'y': 2
            }
            nodes['C'+str(index)] = {
                'x': 2,
                'y': 2
            }

            edges.append({
                'start': 'A'+str(index),
                'end': 'B'+str(index)
            })
            edges.append({
                'start': 'B'+str(index),
                'end': 'C'+str(index)
            })

        for node in ['A','B','C']:
            edges.append({
                'start': node + '0',
                'end': node + '1'
            })

        self.edges = edges
        self.nodes = nodes


    def createGraph(self):
        graph = nx.Graph()

        for label, node in self.nodes.iteritems():
            graph.add_node(label)

        for edge in self.edges:
            if edge['start'][:1] != edge['end'][:1]:
                graph.add_edge(edge['start'], edge['end'], weight = DEPOSITION_RATIO)
            else:
                graph.add_edge(edge['start'], edge['end'], weight = 0)

        self.graph = graph

if __name__ == '__main__':
    input = Input()
    input.readFile('input.json')
    input.createBasicGraph()
    pass