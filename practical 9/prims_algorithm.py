"""
Prim's Algorithm - Minimum Spanning Tree (Greedy Approach)

Time Complexity:
    - Best Case    : O(V^2)
    - Average Case : O(V^2)
    - Worst Case   : O(V^2)

Space Complexity:
    - O(V)
"""

INF = 9999


def prims_mst(graph, n):
    selected = [False] * n
    selected[0] = True
    total_cost = 0

    print("\nEdge  : Weight")

    for _ in range(n - 1):
        min_weight = INF
        u = 0
        v = 0

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] != 0 and graph[i][j] != INF:
                        if graph[i][j] < min_weight:
                            min_weight = graph[i][j]
                            u = i
                            v = j

        print(f"{u} - {v} : {graph[u][v]}")
        total_cost += graph[u][v]
        selected[v] = True

    print("\nMinimum Cost of Spanning Tree =", total_cost)


def main():
    n = int(input("Enter number of vertices: "))

    print("Enter Cost Adjacency Matrix (0 or 9999 for no edge):")

    graph = []
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    prims_mst(graph, n)


if __name__ == "__main__":
    main()
