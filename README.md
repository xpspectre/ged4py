# graph-distance

**ged4py** is an implementation of the graph edit distance for **Python3** and **NetworkX** users.

# How-to use it?
First, you need to create (or load) your graphs using NetworkX. In the following example, we built two simple graphs.

    import networkx as nx
    g=nx.Graph()
    g.add_edge("A","B")

    g.add_node("C",weight=1)
    g2=g.copy()
    g.add_edge("A","C")

Then, use the `compare` function available in the `ged4py.algorithm`

    from ged4py.algorithm import graph_edit_dist
    print(graph_edit_dist.compare(g,g2))

#  Acknowledgments

This is a fork of [**Jacobe2169/ged4py**](https://github.com/Jacobe2169/ged4py) with updates for NetworkX 2 compatibility and some more features.

This library is a modification of the code available at [**haakondr/graph-edit-distance-python**](https://github.com/haakondr/graph-edit-distance-python). The core of the code was implemented by him, thus we'd like to thank him !
