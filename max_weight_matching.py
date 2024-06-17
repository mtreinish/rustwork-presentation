import statistics
import time
import numpy as np
import rustworkx as rx

nodes = []
construct_time = []
times = []
for i in np.logspace(1, 5.5, dtype=int):
    print(i)
    nodes.append(i)
    local_times = []
    build_start = time.perf_counter()
    graph = rx.barabasi_albert_graph(i, 5, seed=123456789)
    build_stop = time.perf_counter()
    construct_time.append(build_stop - build_start)
    #    for _ in range(5):
    start = time.perf_counter()
    rx.max_weight_matching(graph, max_cardinality=True, weight_fn=lambda _: 1)
    #    rx.all_pairs_dijkstra_path_lengths(graph, lambda _: 1.0)
    stop = time.perf_counter()
    times.append(stop - start)
    # times.append(statistics.geometric_mean(local_times))
    print(construct_time)
    print(nodes)
    print(times)
