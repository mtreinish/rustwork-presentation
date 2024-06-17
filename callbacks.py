import rustworkx as rx

graph = rx.PyDiGraph()
graph.extend_from_weighted_edge_list(
    [
        (0, 1, {"weight": 1}),
        (0, 2, {"weight": 2}),
        (1, 3, {"weight": 2}),
        (3, 0, {"weight": 3}),
    ]
)
# Callback weight_fn to return float weight
dist_matrix = rx.floyd_warshall_numpy(
    graph, weight_fn=lambda edge: edge[weight]
)
