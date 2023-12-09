import argparse

def calculate_points(file_path):
    scratchcards = []
    for i in range(300):
        scratchcards.append(1)

    with open(file_path, 'r') as file:

        i = 0
        for line in file:
            text, clean_line = map(str.strip, line.split(':'))
            winning_numbers_str, your_numbers_str = map(str.strip, clean_line.split('|'))

            winning_numbers = set(map(int, winning_numbers_str.split()))
            your_numbers = set(map(int, your_numbers_str.split()))

            matches = len(winning_numbers.intersection(your_numbers))

            for j in range(matches):
                scratchcards[j + i + 1] += scratchcards[i]

            i += 1

    total_scratchcards = sum(scratchcards[0:i])
    return total_scratchcards

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the total points for scratchcards.")
    parser.add_argument("file_path", help="Path to the input file")

    args = parser.parse_args()
    result = calculate_points(args.file_path)
    print(f"The total points for the scratchcards is: {result}")