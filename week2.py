import matplotlib.pyplot as plt
import networkx as nx

# Define the graph
G = nx.Graph()

# Adding nodes (houses)
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")
G.add_node("F")
G.add_node("G")

# Adding edges with weights (distances)
G.add_edge("A", "B", weight=7)
G.add_edge("A", "D", weight=5)
G.add_edge("B", "C", weight=8)
G.add_edge("B", "D", weight=9)
G.add_edge("C", "D", weight=7)
G.add_edge("C", "E", weight=5)
G.add_edge("D", "E", weight=15)
G.add_edge("D", "F", weight=6)
G.add_edge("E", "G", weight=9)
G.add_edge("F", "G", weight=11)

# Draw the graph
pos = nx.spring_layout(G) # positions for all nodes
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Show the plot
plt.show()
