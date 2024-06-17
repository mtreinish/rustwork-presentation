import rustworkx as rx
# Build connectivity graph that models constraints of QPU
connectivity_graph = rx.generators.directed_heavy_hex_graph(9)
for index in connectivity_graph.node_indices():
    connectivity_graph[index] = {"rz", "sx", "x"}
for index in connectivity_graph.edge_indices():
    connectivity_graph.update_edge_by_index(index, {"cx"})
# Build interaction graph of circuit
interaction_graph = rx.PyDiGraph()
interaction_graph.add_nodes_from([set() for _ in range(dag.num_qubits)])
for node in dag.topological_sort():
    if len(node) == 2:
        if interaction_graph.has_edge(*node.qubits):
            interaction_graph.get_edge_data(*node.qubits).add(node.name)
        else:
            interaction_graph.add_edge(*node.qubits, {node.name,})
    else:
        interaction_graph[*node.qubits].add(node.name)
