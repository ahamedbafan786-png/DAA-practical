"""
Breadth First Search (BFS) and Depth First Search (DFS)

Time Complexity:
    - BFS: O(V + E)
    - DFS: O(V + E)

Space Complexity:
    - BFS: O(V)
    - DFS: O(V)
"""


def bfs(graph, start):
    visited = [start]
    queue = [start]

    while queue:
        node = queue.pop(0)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return visited


def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


def main():
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    graph = {}
    print("Enter edges (u v):")
    for _ in range(e):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    start = int(input("\nEnter starting vertex: "))

    print("\nBFS Traversal:", *bfs(graph, start))
    print("DFS Traversal:", *dfs(graph, start))


if __name__ == "__main__":
    main()
