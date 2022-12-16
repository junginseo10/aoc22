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


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2-t1:0.4f} seconds" )
    