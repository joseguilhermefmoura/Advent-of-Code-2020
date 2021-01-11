def get_puzzle_answer() -> int:
    file_input = open("input.txt", "r") # Read the file
    file_lines = file_input.readlines() # Get all lines from it

    file_lines.pop(0) # The first line is useless.

    trees = 0 # Trees encountered
    position = 0 # Starting position
    max_position = 30 

    for line in file_lines: # For each number
        position += 3

        if position > max_position:
            position = position - max_position - 1
        
        if line[position] == '#':
            trees += 1

    return trees
        


def __main__():
    print("Merry Christmas! The answer for this problem is: {0}".format(get_puzzle_answer()))

if __name__ == "__main__":
    __main__()