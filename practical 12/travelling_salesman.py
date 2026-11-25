"""
Travelling Salesman Problem (Dynamic Programming)

Time Complexity:
    - Best Case    : O(n^2 * 2^n)
    - Average Case : O(n^2 * 2^n)
    - Worst Case   : O(n^2 * 2^n)

Space Complexity:
    - O(n * 2^n)
"""

INF = 9999


def tsp(graph, n):
    memo = [[-1] * n for _ in range(1 << n)]
    next_city = [[-1] * n for _ in range(1 << n)]

    def solve(mask, pos):
        if mask == (1 << n) - 1:
            return graph[pos][0]

        if memo[mask][pos] != -1:
            return memo[mask][pos]

        min_cost = INF
        best_next = -1

        for city in range(n):
            if not (mask & (1 << city)):
                cost = graph[pos][city] + solve(mask | (1 << city), city)
                if cost < min_cost:
                    min_cost = cost
                    best_next = city

        memo[mask][pos] = min_cost
        next_city[mask][pos] = best_next
        return min_cost

    min_cost = solve(1, 0)

    path = [0]
    mask = 1
    pos = 0
    while next_city[mask][pos] != -1:
        nxt = next_city[mask][pos]
        path.append(nxt)
        mask |= 1 << nxt
        pos = nxt
    path.append(0)

    return min_cost, path


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
