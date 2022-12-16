from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "sample_input.txt")
#INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

def main():

    ### PART I ###
    with open(INPUT_FILE, mode='rt') as f:        
        sum = 0
        data = f.read().split("\n")
        for i, d in enumerate(data):
            #print(f"Rucksack {i+1}")
            strings = split_list(d)
            comm_char = find_common_char(strings)
            char_index =  get_char_index(comm_char)
            sum += char_index
            #print(f"    Common character: {comm_char} \n    Character Index: {char_index} \n    Current Sum: {sum}")
        print(f"Final Sum is: {sum}")

    ### PART II ###
    with open(INPUT_FILE, mode='rt') as f:
        sum = 0
        data = group_strings(f.read(), 3)
        for i, d in enumerate(data):
            #print(f"Group {i+1}")
            comm_char = find_common_char(tuple(d))
            char_index = get_char_index(comm_char)
            sum += char_index
            #print(f"    Common character: {comm_char} \n    Character Index: {char_index} \n    Current Sum: {sum}")
        print(f"Final Sum is: {sum}")


def group_strings(string, n):
    # Split the input string into a list of lines
    lines = string.strip().split('\n')
    # Assert that the number of lines are divisible by n
    assert len(lines) % n == 0, 'There are orphan lines'
    
    # Initialize an empty list to store the nested lists of 3 lines
    nested_lists = []

    # Iterate over the lines in chunks of 3
    for i in range(0, len(lines), n):
        # Get the chunk of 3 lines
        chunk = lines[i:i+n]
        # Append the chunk to the list of nested lists
        nested_lists.append(chunk)

    return nested_lists
 
                        
def split_list(string_list):
    half = len(string_list) // 2
    return string_list[:half], string_list[half:]


def find_common_char(strings):
    
    # Initialize a set to store the unique characters
    common_chars = set(strings[0])
    
    # Iterate over the lists
    for str in strings[1:]:
        common_chars &= set(str)

    # Assert that there is only one common character
    assert len(common_chars) == 1, "There are multiple common characters"
    
    # Return the only common character
    return next(iter(common_chars))


def get_char_index(char):
   
    # Get the ASCII value of the character
    ascii_value = ord(char)

    # Check if the character is a lowercase letter
    if ascii_value >= 97 and ascii_value <= 122:
        # Return the index of the lowercase letter (1-26)
        return ascii_value - 96

    # Check if the character is an uppercase letter
    if ascii_value >= 65 and ascii_value <= 90:
        # Return the index of the uppercase letter (27-52)
        return ascii_value - 38


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2-t1:0.4f} seconds" )
    