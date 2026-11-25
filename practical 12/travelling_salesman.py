"""
Travelling Salesman Problem (Brute Force / Permutation)

Time Complexity:
    - Best Case    : O(n!)
    - Average Case : O(n!)
    - Worst Case   : O(n!)

Space Complexity:
    - O(n)
"""

INF = 9999


def tsp(graph, n):
    visited = [False] * n
    visited[0] = True
    min_cost = INF
    best_path = []

    def solve(pos, count, cost, path):
        nonlocal min_cost, best_path

        if count == n:
            if graph[pos][0] != INF:
                total = cost + graph[pos][0]
                if total < min_cost:
                    min_cost = total
                    best_path = path + [0]
            return

        for city in range(n):
            if not visited[city] and graph[pos][city] != INF:
                visited[city] = True
                solve(city, count + 1, cost + graph[pos][city], path + [city])
                visited[city] = False

    solve(0, 1, 0, [0])
    return min_cost, best_path


def main():
    n = int(input("Enter number of cities: "))

    print("Enter Cost Matrix (Enter 9999 for no direct path):")

    graph = []
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    min_cost, path = tsp(graph, n)

    print("\nOptimal Path:", " -> ".join(map(str, path)))
    print("Minimum Travelling Cost =", min_cost)


if __name__ == "__main__":
    main()
