# Define a function that multiplies all elements one by one in a list of numbers
def multiply(list_of_numbers: list) -> int:
    result = 1
    for number in list_of_numbers:
         result = result * number 
    return result

def get_puzzle_answer() -> int:
    file_input = open("input.txt", "r") # Read the file
    file_lines = file_input.readlines() # Get all lines from it

    for line in file_lines: # For each number
        for j in file_lines: # Read a new number
            for k in file_lines: # And another one, then check:
                if int(line) + int(j) + int(k) == 2020:
                    # If not solved, check it again. But if solved:
                    file_input.close()
                    return multiply([int(line), int(j), int(k)])


def __main__():
    print("Merry Christmas! The answer for this problem is: {0}".format(get_puzzle_answer()))

if __name__ == "__main__":
    __main__()