from pathlib import Path
import time
import re

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

def main():
    """
    ### PART I ###
    with open(INPUT_FILE, mode='rt') as f:        
        sum = 0
        data = f.read().split("\n")
        for i, d in enumerate(data):
            print(f"Pair {i+1}")
            result = find_containment(d)
            sum += result
            #print(f"    data: {d}\n    result: {result}")
        print(f"Final Sum is: {sum}")
    """

    ### PART II ###
    with open(INPUT_FILE, mode='rt') as f:        
        sum = 0
        data = f.read().split("\n")
        for i, d in enumerate(data):
            print(f"Pair {i+1}")
            result = find_overlap(d)
            sum += result
            #print(f"    data: {d}\n    result: {result}")
        print(f"Final Sum is: {sum}")


def find_containment(str):
    # RegEx the input string into indices of the two list.
    a1, a2, b1, b2 = map(int, re.match(r"(\d+)-(\d+),(\d+)-(\d+)", str).groups())
    a = set(range(a1,a2+1))
    b = set(range(b1,b2+1))
    return a.issubset(b) or a.issuperset(b)
 
def find_overlap(str):
    # RegEx the input string into indices of the two list.
    a1, a2, b1, b2 = map(int, re.match(r"(\d+)-(\d+),(\d+)-(\d+)", str).groups())
    a = set(range(a1,a2+1))
    b = set(range(b1,b2+1))
    return len(a & b) != 0
 
 
                        
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
    