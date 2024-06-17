import rustworkx as rx

simple_graph = rx.PyGraph(multigraph=False)
multi_graph = rx.PyGraph()

simple_graph.extend_from_edge_list(
    [(0, 1), (1, 0)]
)
multi_graph.extend_from_edge_list(
    [(0, 1), (1, 0)]
)
assert simple_graph.num_edges() == 1
assert multi_graph.num_edges() == 2
