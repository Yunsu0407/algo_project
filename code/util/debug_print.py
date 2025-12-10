def print_all_nodes(nodes_dict):
    print("\n=== All Nodes ===")
    for name, node in nodes_dict.items():
        print(f"[ID {node.id}] {name} (lat={node.lat}, lng={node.lng})")


def print_all_edges(nodes_dict):
    print("\n=== All Edges ===")
    for name, node in nodes_dict.items():
        for edge in node.edges:
            print(f"{edge.src.name} → {edge.dst.name} (duration={edge.duration})")
