import argparse

def parse_game_line(line):
    if not line.strip():
        return None, None

    color_map = {"red": 1, "green": 2, "blue": 3}

    game_id_str, subsets_str = map(str.strip, line.split(':'))

    game_id = int(game_id_str.split()[1])

    subsets_list = []
    for subset_str in subsets_str.split(';'):
        subset = {}
        for part in subset_str.split(','):
            count, color = map(str.strip, part.split())
            subset[color_map[color]] = int(count)

        subsets_list.append(subset)

    return game_id, subsets_list

def is_possible_game(subsets):
    cube_configuration = {1: 12, 2: 13, 3: 14}
    for subset in subsets:
        for color, count in subset.items():
            if cube_configuration[color] < count:
                return False
    return True

def calculate_ids_possible_games_sum(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            game_id, subsets = parse_game_line(line)
            if subsets != None and is_possible_game(subsets):
                total_sum += game_id

    return total_sum

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the sum of the IDs of possible games.")
    parser.add_argument("file_path", help="Path to the puzzle file")

    args = parser.parse_args()
    result = calculate_ids_possible_games_sum(args.file_path)
    print(f"The sum of the IDs of possible games is: {result}")
