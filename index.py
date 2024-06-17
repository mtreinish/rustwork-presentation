import rustworkx as rx

graph = rx.PyDiGraph()
node_a = graph.add_node("my_node_a")
node_b = graph.add_node("my_node_b")
assert node_a == 0
assert node_b == 1
graph.add_edge(node_a, node_b, None)
assert "my_node_a" == graph[node_a]
assert "my_node_b" == graph[node_b]
