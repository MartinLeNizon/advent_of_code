import argparse
import re

def words_to_digits(word):
    word_to_digit = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    return word_to_digit.get(word, "0")

def calculate_calibration_sum(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            digits = []
            buffer = ""
            for char in line:
                if char.isdigit():
                    buffer = ""
                    digits.append(char)
                else:
                    buffer += char
                    digit = words_to_digits(buffer)
                    offset = 1

                    while offset < len(buffer):
                        digit_draft = words_to_digits(buffer[offset:])
                        if digit_draft != '0':
                            # print(f"{buffer} ; {offset} ; {digit} ; {digit_draft}")
                            digit = digit_draft
                            break
                        offset += 1

                    if digit != '0':
                        digits.append(digit)

            if len(digits) >= 2:
                calibration_value = int(digits[0] + digits[-1])
                total_sum += calibration_value
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
