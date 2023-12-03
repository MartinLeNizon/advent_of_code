import argparse

last_char_done = []

def get_full_number(engine_schematic, i, j):
    last_digit = [i, j]
    num_str = engine_schematic[i][j]
    for y_offset in range(1, len(engine_schematic[i])-j):
        y_neighbor = j + y_offset
        if engine_schematic[i][y_neighbor].isdigit():
            num_str += engine_schematic[i][y_neighbor]
            last_digit = [i, y_neighbor]
        else:
            break

    for y_offset in range(1, j+1):
        y_neighbor = j - y_offset
        if engine_schematic[i][y_neighbor].isdigit():
            new_num_str = engine_schematic[i][y_neighbor] + num_str
            num_str = new_num_str
        else:
            break

    return int(num_str), last_digit

def get_adjacent_part_numbers(engine_schematic, i, j):
    adjacent_part_numbers = []
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            x_neighbor, y_neighbor = i + x_offset, j + y_offset
            if 0 <= x_neighbor < len(engine_schematic) and 0 <= y_neighbor < len(engine_schematic[i]):
                char = engine_schematic[x_neighbor][y_neighbor]
                if char.isdigit():
                    num, last_digit = get_full_number(engine_schematic, x_neighbor, y_neighbor)

                    # print(f"char: {char} ; num: {num}")
                    if last_digit not in last_char_done:
                        adjacent_part_numbers.append(num)
                        last_char_done.append(last_digit)

    return adjacent_part_numbers

def calculate_sum_part_numbers(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        engine_schematic = [line.strip() for line in file]

        for i in range(len(engine_schematic)):
            for j in range(len(engine_schematic[i])):
                char = engine_schematic[i][j]

                if char == '*':
                    adj_part_numbers = get_adjacent_part_numbers(engine_schematic, i, j)
                    if len(adj_part_numbers) is 2:
                        total_sum += adj_part_numbers[0] * adj_part_numbers[1]

    return total_sum

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the sum of part numbers.")
    parser.add_argument("file_path", help="Path to the input file")

    args = parser.parse_args()
    result = calculate_sum_part_numbers(args.file_path)
    print(f"The sum of part numbers is: {result}")
