import rustworkx as rx

# Create a path graph
g = rx.PyGraph()
g.extend_from_weighted_edge_list([(0, 1, 5), (1, 2, 11), (2, 3, 5)])
# Run max weight matching with max caridnality set to True
matching = rx.max_weight_matching(g, max_cardinality=True, weight_fn=int)
