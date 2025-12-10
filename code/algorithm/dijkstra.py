# dijkstra.py

import heapq
import time


def dijkstra(nodes_dict, start_name, end_name):
    t0 = time.perf_counter()

    # Node 객체 리스트
    nodes = list(nodes_dict.values())
    n = len(nodes)

    INF = float("inf")
    dist = [INF] * n
    prev = [None] * n

    start_id = nodes_dict[start_name].id
    dist[start_id] = 0

    pq = []
    heapq.heappush(pq, (0, start_id))

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for edge in nodes[u].edges:
            v = edge.dst.id
            cost = current_dist + edge.duration

            if cost < dist[v]:
                dist[v] = cost
                prev[v] = u
                heapq.heappush(pq, (cost, v))

    t1 = time.perf_counter()
    exec_time_ms = (t1 - t0) * 1000

    end_id = nodes_dict[end_name].id
    shortest_time = dist[end_id]

    # 경로 복원
    path = reconstruct_path(prev, start_id, end_id, nodes_dict)

    return exec_time_ms, shortest_time, path


def reconstruct_path(prev, start_id, end_id, nodes_dict):
    if prev[end_id] is None and start_id != end_id:
        return []

    path_ids = []
    cur = end_id
    while cur is not None:
        path_ids.append(cur)
        cur = prev[cur]

    path_ids.reverse()

    id_to_name = {node.id: node.name for node in nodes_dict.values()}
    return [id_to_name[i] for i in path_ids]
