# Read the file
file_input = open("input.txt", "r")

# Read all lines of it
file_lines = file_input.readlines()

def find_numbers():
    for i in range(0, len(file_lines)):
        current_line = int(file_lines[i])
        for j in file_lines:
            aux = current_line
            aux += int(j)
            if aux == 2020:
                return [current_line, int(j)]

# Get the numbers we want
numbers = find_numbers()

# Multiply them
result = numbers[0] * numbers[1]

print("Merry Christmas! The answer for this problem is: {0}".format(result))

# Closes the file
file_input.close()