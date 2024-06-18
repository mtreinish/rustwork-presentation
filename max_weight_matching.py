import statistics
import time
import numpy as np
import rustworkx as rx

nodes = []
times = []
for i in np.logspace(1, 5.5, dtype=int):
    print(i)
    nodes.append(i)
    local_times = []
    graph = rx.barabasi_albert_graph(i, 5, seed=123456789)
    for _ in range(5):
        start = time.perf_counter()
        rx.max_weight_matching(graph, max_cardinality=True, weight_fn=lambda _: 1)
        stop = time.perf_counter()
        local_times.append(stop - start)
    times.append(statistics.geometric_mean(local_times))
    print(nodes)
    print(times)
