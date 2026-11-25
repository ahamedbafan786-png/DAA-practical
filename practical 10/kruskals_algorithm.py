"""
Kruskal's Algorithm - Minimum Spanning Tree (Greedy Approach)

Time Complexity:
    - Best Case    : O(E log E)
    - Average Case : O(E log E)
    - Worst Case   : O(E log E)

Space Complexity:
    - O(V + E)
"""


def find(parent, i):
    while parent[i] != i:
        i = parent[i]
    return i


def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


def kruskal_mst(n, edges):
    edges.sort(key=lambda edge: edge[2])

    parent = [i for i in range(n)]
    rank = [0] * n
    mst = []
    total_cost = 0

    for u, v, w in edges:
        root_u = find(parent, u)
        root_v = find(parent, v)

        if root_u != root_v:
            mst.append((u, v, w))
            total_cost += w
            union(parent, rank, root_u, root_v)

            if len(mst) == n - 1:
                break

    print("\nEdge  : Weight")
    for u, v, w in mst:
        print(f"{u} - {v} : {w}")

    print("\nMinimum Cost of Spanning Tree =", total_cost)


def main():
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))

    edges = []
    print("Enter edges (u v weight):")
    for _ in range(e):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    kruskal_mst(n, edges)


if __name__ == "__main__":
    main()
