import argparse

def is_valid_symbol(char):
    # Helper function to check if a character is a valid symbol
    return char not in ('.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

def calculate_sum_part_numbers(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        engine_schematic = [line.strip() for line in file]

        last_char = [-1, -1]

        for i in range(len(engine_schematic)):
            for j in range(len(engine_schematic[i])):
                char = engine_schematic[i][j]

                current_char = [i, j]

                if char.isdigit() and any(
                    is_valid_symbol(engine_schematic[x][y])
                    for x in range(i - 1, i + 2)
                    for y in range(j - 1, j + 2)
                    if 0 <= x < len(engine_schematic) and 0 <= y < len(engine_schematic[i])
                ):

                    num_str = char
                    for y_offset in range(1, len(engine_schematic[i])-j):
                        y_neighbor = j + y_offset
                        if engine_schematic[i][y_neighbor].isdigit():
                            num_str += engine_schematic[i][y_neighbor]
                            current_char = [i, y_neighbor]
                        else:
                            break

                    for y_offset in range(1, j+1):
                        y_neighbor = j - y_offset
                        if engine_schematic[i][y_neighbor].isdigit():
                            new_num_str = engine_schematic[i][y_neighbor] + num_str
                            num_str = new_num_str
                        else:
                            break

                    if current_char != last_char:
                        total_sum += int(num_str)

                last_char = current_char


    return total_sum

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the sum of part numbers.")
    parser.add_argument("file_path", help="Path to the input file")

    args = parser.parse_args()
    result = calculate_sum_part_numbers(args.file_path)
    print(f"The sum of part numbers is: {result}")
