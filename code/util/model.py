# model.py


class Node:
    def __init__(self, id, name, lat, lng):
        self.id = id
        self.name = name
        self.lat = lat  # 위도
        self.lng = lng  # 경도
        self.edges = []  # 연결된 Edge들

    def add_edge(self, edge):
        self.edges.append(edge)


class Edge:
    def __init__(self, src, dst, duration):
        self.src = src
        self.dst = dst
        self.duration = duration
