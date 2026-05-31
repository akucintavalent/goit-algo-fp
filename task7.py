import random
from collections import Counter

import matplotlib.pyplot as plt


ANALYTICAL_PROBABILITIES = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}


def throw_two_dice() -> int:
    return random.randint(1, 6) + random.randint(1, 6)


def monte_carlo_simulation(throws_count: int) -> dict[int, float]:
    frequencies = Counter(throw_two_dice() for _ in range(throws_count))
    return {dice_sum: frequencies[dice_sum] / throws_count for dice_sum in range(2, 13)}


def print_comparison_table(probabilities: dict[int, float]) -> None:
    print("Sum | Monte Carlo | Analytical | Difference")
    print("----|-------------|------------|-----------")

    for dice_sum in range(2, 13):
        monte_carlo = probabilities[dice_sum]
        analytical = ANALYTICAL_PROBABILITIES[dice_sum]
        difference = abs(monte_carlo - analytical)
        print(
            f"{dice_sum:>3} | "
            f"{monte_carlo * 100:>10.2f}% | "
            f"{analytical * 100:>9.2f}% | "
            f"{difference * 100:>8.2f}%"
        )


def plot_probabilities(probabilities: dict[int, float]) -> None:
    sums = list(range(2, 13))
    monte_carlo_values = [probabilities[dice_sum] * 100 for dice_sum in sums]
    analytical_values = [ANALYTICAL_PROBABILITIES[dice_sum] * 100 for dice_sum in sums]

    plt.figure(figsize=(10, 5))
    plt.plot(sums, monte_carlo_values, marker="o", label="Monte Carlo")
    plt.plot(sums, analytical_values, marker="s", label="Analytical")
    plt.title("Probability of sums when rolling two dice")
    plt.xlabel("Sum")
    plt.ylabel("Probability, %")
    plt.xticks(sums)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()


def main() -> None:
    throws_count = int(input("Enter the number of dice throws (1-1000000): "))
    if throws_count < 1 or throws_count > 1_000_000:
        print("Please enter a number between 1 and 1000000.")
        return

    probabilities = monte_carlo_simulation(throws_count)
    print_comparison_table(probabilities)
    plot_probabilities(probabilities)

    max_difference = max(
        abs(probabilities[dice_sum] - ANALYTICAL_PROBABILITIES[dice_sum])
        for dice_sum in range(2, 13)
    )
    print(
        "\nConclusion: Monte Carlo probabilities approach analytical values "
        f"as the number of throws grows. Max difference: "
        f"{max_difference * 100:.2f}%."
    )


if __name__ == "__main__":
    main()
