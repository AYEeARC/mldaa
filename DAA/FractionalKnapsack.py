# Fractional Knapsack

def fractional_knapsack(weights, profits, capacity):

    items = []

    for i in range(len(weights)):
        ratio = profits[i] / weights[i]
        items.append((ratio, weights[i], profits[i], i + 1))

    # Sort according to profit/weight ratio
    items.sort(reverse=True)

    total_profit = 0
    remaining_capacity = capacity

    for ratio, weight, profit, item_no in items:

        if remaining_capacity == 0:
            break

        if weight <= remaining_capacity:
            # Take complete item
            remaining_capacity -= weight
            total_profit += profit

            print("Item", item_no, ": Taken completely")

        else:
            # Take fraction of item
            fraction = remaining_capacity / weight
            total_profit += profit * fraction

            print("Item", item_no, ": Taken",
                  round(fraction * 100, 2), "%")

            remaining_capacity = 0

    print("\nMaximum Profit:", total_profit)


# Input
weights = [10, 20, 30]
profits = [60, 100, 120]
capacity = 100

fractional_knapsack(weights, profits, capacity)