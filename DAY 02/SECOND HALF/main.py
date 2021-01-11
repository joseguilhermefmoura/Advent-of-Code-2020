def get_puzzle_answer() -> int:
    file_input = open("input.txt", "r") # Read the file
    file_lines = file_input.readlines() # Get all lines from it

    result = 0

    for line in file_lines:
        # For each line, get all the informations we need:
        line_info = line.split(' ')

        password = line_info[2]
        position_one = int(line_info[0].split('-')[0])
        position_two = int(line_info[0].split('-')[1])
        rule = line_info[1][0]

        # If it is valid, add it to the result
        if password[(position_one - 1)] == rule:
            if password[(position_two) - 1] != rule:
                result += 1
        else:
            if password[(position_two - 1)] == rule:
                result += 1

    return result


def __main__():
    print("Merry Christmas! The answer for this problem is: {0}".format(get_puzzle_answer()))

if __name__ == "__main__":
    __main__()