# 0/1 Knapsack using Dynamic Programming

def knapsack(weights, profits, capacity):

    n = len(weights)

    # DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):

        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:

                dp[i][w] = max(
                    profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )

            else:
                dp[i][w] = dp[i - 1][w]

    print("Maximum Profit:", dp[n][capacity])

    # Find selected items
    w = capacity
    selected_items = []

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            selected_items.append(i)
            w -= weights[i - 1]

    selected_items.reverse()

    print("Selected Items:", selected_items)

    print("\nDP Table:")

    for row in dp:
        print(row)


weights = [10, 20, 30]
profits = [60, 100, 120]
capacity = 50

knapsack(weights, profits, capacity)