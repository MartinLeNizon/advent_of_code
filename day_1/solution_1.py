import argparse

def calculate_calibration_sum(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            digits = [char for char in line if char.isdigit()]

            if len(digits) >= 2:
                calibration_value = int(digits[0] + digits[-1])
            elif len(digits) == 1:
                calibration_value = int(digits[0] + digits[0])

            total_sum += calibration_value

    return total_sum

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the sum of calibration values from a file.")
    parser.add_argument("file_path", help="Path to the calibration file")

    args = parser.parse_args()
    result = calculate_calibration_sum(args.file_path)
    print(f"The sum of calibration values is: {result}")
