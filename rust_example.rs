use rustworkx_core::petgraph;
use rustworkx_core::max_weight_matching::max_weight_matching;

// Create a path graph
let g = petgraph::graph::UnGraph::<i32, i128>::from_edges(&[
    (1, 2, 5), (2, 3, 11), (3, 4, 5)
]);
// Run max weight matching with max cardinality set to true
let matching = max_weight_matching(&g, true, |e| Ok(*e.weight()), true);
