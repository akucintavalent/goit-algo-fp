import uuid
from collections import deque
from typing import Dict, Tuple, Generator, Any

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
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
        font_color="white",
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


# Task 4
def build_heap_tree(heap: list) -> Node:
    if not heap:
        return None

    root = Node(heap[0])
    queue = deque([root])
    i = 1

    while queue and i < len(heap):
        current = queue.popleft()
        current.left = Node(heap[i])
        queue.append(current.left)
        i += 1

        if i < len(heap):
            current.right = Node(heap[i])
            queue.append(current.right)
            i += 1

    return root


# Task 5
def gray_colors(n: int) -> Generator[str, None, None]:
    for i in range(0, 256, 255 // n):
        yield f"#{i:02x}{i:02x}{i:02x}"


def copy_tree(node: Node) -> Node:
    if node is None:
        return None

    new_node = Node(node.val, color=node.color)
    new_node.left = copy_tree(node.left)
    new_node.right = copy_tree(node.right)

    return new_node


def bfs_visualize(tree_root: Node, n: int) -> None:
    if tree_root is None:
        return

    root = copy_tree(tree_root)  # Створюємо копію дерева для візуалізації

    queue = deque([root])
    color_gen = gray_colors(n)

    while queue:
        current = queue.popleft()
        current.color = next(color_gen)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    draw_tree(root)


def dfs_visualize(tree_root: Node, n: int) -> Node:
    if tree_root is None:
        return None

    root = copy_tree(tree_root)  # Створюємо копію дерева для візуалізації

    stack = [root]
    color_gen = gray_colors(n)

    while stack:
        current = stack.pop()
        current.color = next(color_gen)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

    draw_tree(root)


def main() -> None:
    n = int(input("Enter the numb er of elements in the heap (up to 15): "))
    if n < 1 or n > 15:
        print("Please enter a number between 1 and 15.")
        return

    rand_int_list = [random.randint(1, 100) for _ in range(n)]
    print("Random integer array:", rand_int_list)

    heapq.heapify(rand_int_list)
    print("Min-heap:", rand_int_list)

    heap = rand_int_list

    heap_tree_root = build_heap_tree(heap)
    draw_tree(heap_tree_root)

    print("Visualizing BFS traversal...")
    bfs_visualize(heap_tree_root, n)

    print("Visualizing DFS traversal...")
    dfs_visualize(heap_tree_root, n)


if __name__ == "__main__":
    main()
