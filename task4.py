import uuid
from typing import Dict, Tuple

import networkx as nx
import matplotlib.pyplot as plt

import random
import heapq


class Node:
    def __init__(self, key: int, color: str = "skyblue") -> None:
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(
    graph: nx.Graph,
    node: Node,
    pos: Dict[str, Tuple[float, float]],
    x: float = 0,
    y: float = 0,
    layer: int = 1,
) -> nx.Graph:
    if node is None:
        return graph

    graph.add_node(node.id, color=node.color, label=node.val)

    if node.left:
        graph.add_edge(node.id, node.left.id)
        l = x - 1 / (2**layer)
        pos[node.left.id] = (l, y - 1)
        add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)

    if node.right:
        graph.add_edge(node.id, node.right.id)
        r = x + 1 / (2**layer)
        pos[node.right.id] = (r, y - 1)
        add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

    return graph


def draw_tree(tree_root: Node) -> None:
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [data.get("color", "skyblue") for _, data in tree.nodes(data=True)]
    labels = {node: data.get("label") for node, data in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def _build_sample_tree() -> Node:
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    return root


def build_heap_tree(heap: list) -> Node:
    if not heap:
        return None

    root = Node(heap[0])
    queue = [root]
    i = 1

    while queue and i < len(heap):
        current = queue.pop(0)
        current.left = Node(heap[i])
        queue.append(current.left)
        i += 1

        if i < len(heap):
            current.right = Node(heap[i])
            queue.append(current.right)
            i += 1

    return root


def main() -> None:
    rand_int_list = [random.randint(1, 100) for _ in range(random.randint(5, 15))]
    print("Random integer array:", rand_int_list)

    heapq.heapify(rand_int_list)
    print("Min-heap:", rand_int_list)

    heap = rand_int_list

    heap_tree_root = build_heap_tree(heap)
    draw_tree(heap_tree_root)


if __name__ == "__main__":
    main()
