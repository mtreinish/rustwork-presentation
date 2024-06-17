def _target_match(a, b):
    return a.issuperset(b)
# Return an iterator of subgraphs mappings:
subgraphs = vf2_mapping(
    connectivity_graph,
    interaction_graph,
    node_matcher=_target_match,
    edge_matcher=_target_match,
    subgraph=True,
    id_order=False,
    induced=False,
)
best_layout = min(subgraphs, key=scoring_function)
