import networkx as nx
import heapq
import matplotlib.pyplot as plt


def create_weighted_graph() -> nx.Graph:
    G = nx.Graph()
    G.add_edge("A", "B", weight=1)
    G.add_edge("A", "C", weight=4)
    G.add_edge("B", "C", weight=2)
    G.add_edge("B", "D", weight=5)
    G.add_edge("C", "D", weight=1)
    G.add_edge("C", "E", weight=3)
    G.add_edge("D", "E", weight=2)
    G.add_edge("D", "F", weight=7)
    return G


def dijkstra(graph: nx.Graph, start: str) -> dict:
    distances = {node: float("inf") for node in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]["weight"]
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def main():
    graph = create_weighted_graph()

    start_node = "A"
    shortest_paths = dijkstra(graph, start_node)

    print(f"Shortest paths from node {start_node}:")
    for node, distance in shortest_paths.items():
        print(f"Distance to {node}: {distance}")

    pos = nx.spring_layout(graph)

    nx.draw(
        graph, pos=pos, with_labels=True, node_color="lightblue", font_weight="bold"
    )
    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=edge_labels)
    plt.show()


if __name__ == "__main__":
    main()
