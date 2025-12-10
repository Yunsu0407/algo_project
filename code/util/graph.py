# graph1.py

from util.model import Node, Edge
from util.kakao import get_all_coord
from util.osrm import get_osrm_route_cached


# case1, case2 공통 사용
def make_graph(building_list):
    # 건물 리스트 → 좌표 가져오기
    coord_list = get_all_coord(building_list)

    # Node 생성
    nodes = {}  # name → Node
    for idx, item in enumerate(coord_list):
        name = item["name"]
        lat, lng = item["coord"]
        node = Node(id=idx, name=name, lat=lat, lng=lng)
        nodes[name] = node

    # Edge 생성 (OSRM 요청)
    for src in nodes.values():
        for dst in nodes.values():
            if src.id == dst.id:
                continue

            duration = get_osrm_route_cached(src, dst)
            edge = Edge(src, dst, duration)
            src.add_edge(edge)

    return nodes


# 이하 함수는 case2에서 사용
def get_node_name(building, floor):
    if not floor:
        return building
    return f"{building}-{floor}"


# src_node.edges 중에 같은 dst를 가진 edge가 있으면 duration을 갱신한다. 존재하지 않는다면 새로 추가한다.
def update_or_add_edge(src_node, dst_node, duration):

    # 기존 엣지 존재하면 갱신
    for edge in src_node.edges:
        if edge.dst.id == dst_node.id:
            # 기존 duration보다 짧으면 갱신
            if duration < edge.duration:
                edge.duration = duration
            return

    # 없으면 새로 추가
    src_node.add_edge(Edge(src_node, dst_node, duration))


def apply_edge_list(nodes_dict, edge_list):
    # ===== 1) 층 노드 자동 생성 =====
    for item in edge_list:
        base_name = item["src"]
        src_name = get_node_name(item["src"], item["src_floor"])
        dst_name = get_node_name(item["dst"], item["dst_floor"])

        # src 층 노드 생성
        if src_name not in nodes_dict:
            base = nodes_dict[item["src"]]
            nodes_dict[src_name] = Node(
                id=len(nodes_dict),
                name=src_name,
                lat=base.lat,
                lng=base.lng,
            )

        # dst 층 노드 생성
        if dst_name not in nodes_dict:
            base = nodes_dict[item["dst"]]
            nodes_dict[dst_name] = Node(
                id=len(nodes_dict),
                name=dst_name,
                lat=base.lat,
                lng=base.lng,
            )

    # ===== 2) 건물 ↔ 층 간 Edge 연결(duration = 0) =====
    for name, node in list(nodes_dict.items()):
        # "학림관-1F" 같은 층 노드인지 확인
        if "-" in name:
            building_name, floor = name.split("-", 1)

            # 건물 본체 노드가 존재하는 경우에만 0비용 연결
            if building_name in nodes_dict:
                building_node = nodes_dict[building_name]
                floor_node = node

                # 양방향 연결
                update_or_add_edge(building_node, floor_node, 0)
                update_or_add_edge(floor_node, building_node, 0)

    # ===== 3) edge_list 기반 Edge 추가 (갱신 포함) =====
    for item in edge_list:
        src_name = get_node_name(item["src"], item["src_floor"])
        dst_name = get_node_name(item["dst"], item["dst_floor"])

        src_node = nodes_dict[src_name]
        dst_node = nodes_dict[dst_name]

        duration = item["duration"]

        # 갱신 또는 추가
        update_or_add_edge(src_node, dst_node, duration)
        # 필요하면 양방향
        update_or_add_edge(dst_node, src_node, duration)
