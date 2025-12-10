# bellman_ford.py

import time


def bellman_ford(nodes_dict, start_name, end_name):
    t0 = time.perf_counter()

    nodes = list(nodes_dict.values())
    n = len(nodes)
    INF = float("inf")
    dist = [INF] * n
    prev = [None] * n

    start_id = nodes_dict[start_name].id
    dist[start_id] = 0

    # 모든 엣지를 일괄 리스트로 수집
    edges = []
    for src in nodes:
        for edge in src.edges:
            edges.append((src.id, edge.dst.id, edge.duration))

    # N-1번 완화
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                updated = True
        if not updated:
            break

    # t0 ~ t1 시간 측정
    t1 = time.perf_counter()
    exec_time_ms = (t1 - t0) * 1000

    end_id = nodes_dict[end_name].id
    shortest_time = dist[end_id]

    # 경로 복원
    path = reconstruct_path(prev, start_id, end_id, nodes_dict)

    return exec_time_ms, shortest_time, path


def reconstruct_path(prev, start_id, end_id, nodes_dict):
    if prev[end_id] is None and end_id != start_id:
        return []

    path_ids = []
    cur = end_id
    while cur is not None:
        path_ids.append(cur)
        cur = prev[cur]

    path_ids.reverse()

    id_to_name = {node.id: node.name for node in nodes_dict.values()}
    return [id_to_name[i] for i in path_ids]
