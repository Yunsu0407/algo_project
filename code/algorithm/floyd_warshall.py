# floyd_warshall.py

import time


def floyd_warshall(nodes_dict):
    nodes = list(nodes_dict.values())
    n = len(nodes)

    INF = float("inf")
    dist = [[INF] * n for _ in range(n)]
    next_node = [[None] * n for _ in range(n)]

    # 자기 자신 거리 0
    for node in nodes:
        dist[node.id][node.id] = 0

    # 엣지 기반 초기화
    for src in nodes:
        for edge in src.edges:
            dst = edge.dst
            dist[src.id][dst.id] = edge.duration
            next_node[src.id][dst.id] = dst.id

    # Floyd–Warshall 3중 루프
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    return dist, next_node


def reconstruct_path(start_id, end_id, next_node):
    """id 기반 경로 복원"""
    if next_node[start_id][end_id] is None:
        return []

    path = [start_id]
    while start_id != end_id:
        start_id = next_node[start_id][end_id]
        path.append(start_id)
    return path


def get_path_by_name(nodes_dict, next_node, start_name, end_name):
    """이름 기반 경로 복원"""
    start_id = nodes_dict[start_name].id
    end_id = nodes_dict[end_name].id

    path_ids = reconstruct_path(start_id, end_id, next_node)
    id_to_name = {node.id: node.name for node in nodes_dict.values()}
    return [id_to_name[i] for i in path_ids]


def floyd_warshall_shortest(nodes_dict, start_name, end_name):
    t0 = time.perf_counter()

    dist, next_node = floyd_warshall(nodes_dict)

    t1 = time.perf_counter()
    exec_time_ms = (t1 - t0) * 1000  # ms 변환

    # 최단 시간
    start_id = nodes_dict[start_name].id
    end_id = nodes_dict[end_name].id
    shortest_time = dist[start_id][end_id]

    # 경로 복구
    path = get_path_by_name(nodes_dict, next_node, start_name, end_name)

    return exec_time_ms, shortest_time, path
