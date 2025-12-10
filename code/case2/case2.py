# case1.py

import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CODE_DIR = os.path.join(ROOT_DIR, "code")

sys.path.append(ROOT_DIR)
sys.path.append(CODE_DIR)


from pprint import pprint
from data.list import building_list, edge_list
from util.graph import make_graph, apply_edge_list
from algorithm.bellman_ford import bellman_ford
from algorithm.dijkstra import dijkstra
from algorithm.floyd_warshall import floyd_warshall_shortest

from util.debug_print import print_all_nodes, print_all_edges
from util.visualize import visualize_graph


def main():
    nodes = make_graph(building_list)
    apply_edge_list(nodes, edge_list)  # case2 확장 (floor + duration override)
    # pprint(nodes)

    print("--Case2--")
    print("Bellman Ford-----------------------------------------------------")
    pprint(bellman_ford(nodes, "동국대학교 학림관", "동국대학교 중앙도서관"))

    print("Dijkstra---------------------------------------------------------")
    pprint(dijkstra(nodes, "동국대학교 학림관", "동국대학교 중앙도서관"))

    print("Floyd-Warshall---------------------------------------------------")
    pprint(floyd_warshall_shortest(nodes, "동국대학교 학림관", "동국대학교 중앙도서관"))

    # print_all_nodes(nodes)
    # print_all_edges(nodes)
    visualize_graph(nodes, "case2_graph")


def excute_case2():
    nodes = make_graph(building_list)
    apply_edge_list(nodes, edge_list)
    return nodes


if __name__ == "__main__":
    main()
