# visualize.py

from graphviz import Digraph
import os


def visualize_graph(nodes, output_name="graph"):
    # 현재 파일(util/visualize.py)의 위치 기준으로 루트 경로 탐색
    ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    DATA_DIR = os.path.join(ROOT_DIR, "data")
    os.makedirs(DATA_DIR, exist_ok=True)

    output_path = os.path.join(DATA_DIR, output_name)

    dot = Digraph(format="png")
    dot.attr(fontname="Malgun Gothic")
    dot.attr("node", fontname="Malgun Gothic")
    dot.attr("edge", fontname="Malgun Gothic")

    # 노드 추가
    for name, node in nodes.items():
        dot.node(str(node.id), name)

    # 엣지 추가
    for _, node in nodes.items():
        for edge in node.edges:
            dot.edge(str(edge.src.id), str(edge.dst.id), label=str(edge.duration))

    dot.render(output_path, view=True)
