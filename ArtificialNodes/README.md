**Articial Node Addition**

This module is concerned with the addition of artificial node to model the problem at hand, by utilizing the TSP algorithm.

First, we read the file for the input to the artificial node module. The input to the module is in JSON format. The format is the following:
~~~~
{
    "nodes":[
        {
            "id": "node_label",
            "X": node_x,
            "Y": node_y
        },
        ...
    ],
    "edges":[
        {
            "start" : "start_node_label",
            "end": "end_node_label"
        }
    ]
}
~~~~

Then, we construct the graph using the walls as the edges and the corners of the walls as nodes.

Thereon, we add additional nodes as per the degree of the each of the node. At the end of this part, the number of nodes would be twice the number of edges in the original graph.

Finally, we compute the cost of the deposition edges.