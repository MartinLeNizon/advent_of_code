import argparse

def calculate_points(file_path):
    total_points = 0

    with open(file_path, 'r') as file:
        for line in file:
            text, clean_line = map(str.strip, line.split(':'))
            winning_numbers_str, your_numbers_str = map(str.strip, clean_line.split('|'))

            winning_numbers = set(map(int, winning_numbers_str.split()))
            your_numbers = set(map(int, your_numbers_str.split()))

            common_numbers = winning_numbers.intersection(your_numbers)

            points = 2 ** (len(common_numbers) - 1) if len(common_numbers) > 0 else 0

            total_points += points

    return total_points

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the total points for scratchcards.")
    parser.add_argument("file_path", help="Path to the input file")

    args = parser.parse_args()
    result = calculate_points(args.file_path)
    print(f"The total points for the scratchcards is: {result}")