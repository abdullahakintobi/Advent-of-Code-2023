# Function to extract the first and last digits from a line
def extract_digits(line):
    first_digit = None
    last_digit = None
    for char in line:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            last_digit = char
    return int(first_digit + last_digit) if first_digit and last_digit else 0

# Main function to process the text file
def sum_digits_from_file(filename):
    total_sum = 0
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if line:  # If line is not empty
                number = extract_digits(line)
                total_sum += number
    return total_sum

# Usage
filename = 'input.txt'
total_sum = sum_digits_from_file(filename)
print(total_sum)
