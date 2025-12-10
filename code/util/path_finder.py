# path_finder.py

import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

from algorithm.floyd_warshall import floyd_warshall, reconstruct_path
from case1.case1 import excute_case1
from case2.case2 import excute_case2


def find_improved_paths(nodes_case1, nodes_case2):
    dist1, _ = floyd_warshall(nodes_case1)
    dist2, next2 = floyd_warshall(nodes_case2)

    improved = []

    # 같은 원본 건물만 비교하기 위해 이름 목록 정리
    names_case1 = list(nodes_case1.keys())
    names_case2 = list(nodes_case2.keys())

    # case1에 있고 case2에도 존재하는 노드들만 비교
    common_names = [name for name in names_case1 if name in names_case2]

    for start in common_names:
        for end in common_names:
            start_id1 = nodes_case1[start].id
            end_id1 = nodes_case1[end].id

            start_id2 = nodes_case2[start].id
            end_id2 = nodes_case2[end].id

            before = dist1[start_id1][end_id1]
            after = dist2[start_id2][end_id2]

            if before == float("inf"):
                continue

            if after < before:
                path_ids = reconstruct_path(start_id2, end_id2, next2)
                id_to_name = {node.id: node.name for node in nodes_case2.values()}
                path = [id_to_name[p] for p in path_ids]

                improved.append(
                    {
                        "start": start,
                        "end": end,
                        "before": before,
                        "after": after,
                        "path": path,
                    }
                )

    return improved


def main():
    nodes_case1 = excute_case1()
    nodes_case2 = excute_case2()

    improved = find_improved_paths(nodes_case1, nodes_case2)

    print("\n=== 단축된 경로 목록 ===")
    for item in improved:
        print(f"{item['start']} → {item['end']}")
        print(f"  before: {item['before']:.2f}")
        print(f"  after : {item['after']:.2f}")
        print("  path  :", " → ".join(item["path"]))
        print()


if __name__ == "__main__":
    main()
