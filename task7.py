import random


def throw_a_dice() -> int:
    return random.randint(1, 6)


def throw_a_dice_twice() -> list:
    return [throw_a_dice() for _ in range(2)]


def sum_of_dice(dice: list) -> int:
    return sum(dice)


def throw_two_dice_n_times(n: int) -> list:
    return [sum_of_dice(throw_a_dice_twice()) for _ in range(n)]


def calculate_frequencies(results: list) -> dict:
    frequencies = {i: 0 for i in range(2, 13)}
    for result in results:
        frequencies[result] += 1
    return frequencies


def calculate_probabilities(frequencies: dict, total_throws: int) -> dict:
    probabilities = {key: value / total_throws for key, value in frequencies.items()}
    return probabilities


def main():
    n = int(input("Enter the number of times to throw two dice (up to 10000): "))
    if n < 1 or n > 10000:
        print("Please enter a number between 1 and 10000.")
        return

    results = throw_two_dice_n_times(n)
    frequencies = calculate_frequencies(results)
    probabilities = calculate_probabilities(frequencies, n)

    print("Sum\tFrequency\tProbability")
    for sum_value in range(2, 13):
        print(
            f"{sum_value}\t{frequencies[sum_value]}\t\t{probabilities[sum_value]:.4f}"
        )


if __name__ == "__main__":
    main()
