"""
Coin Change Problem - Making Change (Dynamic Programming)

Time Complexity: O(n * amount)

Space Complexity: O(amount)
"""


def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] != float("inf"):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


def main():
    n = int(input("Enter number of coins: "))
    coins = list(map(int, input("Enter coins:\n").split()))
    amount = int(input("Enter amount: "))

    result = coin_change(coins, amount)

    if result != -1:
        print("\nMinimum number of coins needed =", result)
    else:
        print("\nChange cannot be made with given coins.")


if __name__ == "__main__":
    main()
