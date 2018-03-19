import networkx as nx
from ged4py.algorithm import graph_edit_dist

g1 = nx.Graph()
g1.add_edge("A", "B")
g1.add_node("C", weight=1)

g2 = g1.copy()
g1.add_edge("A", "C")

ged = graph_edit_dist.compare(g1, g2, print_details=True, normalized=False)
print(ged)

############################################

# g1 = nx.Graph()
# g1.add_edge("A", "B")
# g1.add_edge("B", "C")
#
# g2 = g1.copy()
# g2.add_edge("A", "C")
#
# ged = graph_edit_dist.compare(g1, g2, print_details=True, normalized=False)
# print(ged)
