import rustworkx as rx

graph = rx.PyGraph()
graph.extend_from_edge_list([(0, 1), (1, 2)])
assert graph.has_edge(1, 0)
digraph = rx.PyDiGraph()
digraph.extend_from_edge_list([(0, 1), (1, 2)])
assert not digraph.has_edge(1, 0)
