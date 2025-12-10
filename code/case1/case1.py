# case1.py

import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CODE_DIR = os.path.join(ROOT_DIR, "code")

sys.path.append(ROOT_DIR)
sys.path.append(CODE_DIR)


from pprint import pprint
from data.list import building_list
from util.graph import make_graph
from algorithm.bellman_ford import bellman_ford
from algorithm.dijkstra import dijkstra
from algorithm.floyd_warshall import floyd_warshall_shortest

from util.debug_print import print_all_nodes, print_all_edges
from util.visualize import visualize_graph


def main():
    nodes = make_graph(building_list)
    # pprint(nodes)

    print("--Case1--")
    print("Bellman Ford-----------------------------------------------------")
    pprint(bellman_ford(nodes, "동국대학교 학림관", "동국대학교 중앙도서관"))

    print("Dijkstra---------------------------------------------------------")
    pprint(dijkstra(nodes, "동국대학교 학림관", "동국대학교 중앙도서관"))

    print("Floyd-Warshall---------------------------------------------------")
    pprint(floyd_warshall_shortest(nodes, "동국대학교 학림관", "동국대학교 중앙도서관"))

    # print_all_nodes(nodes)
    # print_all_edges(nodes)
    visualize_graph(nodes, "case1_graph")


def excute_case1():
    nodes = make_graph(building_list)
    return nodes


if __name__ == "__main__":
    main()
