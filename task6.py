def greedy_algorithm(items: dict, budget: int) -> list:
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    selected_items = []
    total_cost = 0

    for item, details in sorted_items:
        if total_cost + details["cost"] <= budget:
            selected_items.append(item)
            total_cost += details["cost"]

    return selected_items


def dynamic_programming(items: dict, budget: int) -> list:
    item_list = list(items.items())
    n = len(item_list)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name, details = item_list[i - 1]
        cost = details["cost"]
        calories = details["calories"]

        for j in range(budget + 1):
            if cost <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)
            else:
                dp[i][j] = dp[i - 1][j]

    selected_items = []
    j = budget

    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            item_name, details = item_list[i - 1]
            selected_items.append(item_name)
            j -= details["cost"]

    return selected_items[::-1]


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    budget = int(input("Enter your budget (up to 200): "))
    if budget < 1 or budget > 200:
        print("Please enter a budget between 1 and 200.")
        return

    print("\nGreedy Algorithm Result:")
    greedy_result = greedy_algorithm(items, budget)
    print(greedy_result)

    print("\nDynamic Programming Result:")
    dp_result = dynamic_programming(items, budget)
    print(dp_result)


if __name__ == "__main__":
    main()
