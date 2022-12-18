from pathlib import Path
from collections import deque
import time
import re

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

def main():
    
    ### PART I ###
    with open(INPUT_FILE, mode='rt') as f:        
        signals = f.read().split("\n") # split the input text into initial state and move lines
        
        for i, signal in enumerate(signals):
            print(f"Checking Datastream #{i+1}: {signal}")
            sub = Subroutine()
            index = -1
            for j, char in enumerate(signal):
                if sub.check():
                    index = sub.counter
                    break
                else:
                    sub.add_char(char)
            print(f"index: {index}")
            
                
class Subroutine:
        
    def __init__(self):
        self.buffer = deque([],maxlen=14)
        self.counter = 0
    
    def add_char(self, char):
        self.buffer.append(char)
        self.counter += 1

    def check(self):        
        return len(set(self.buffer)) == len(self.buffer) and self.counter > 3
    
    


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2-t1:0.4f} seconds" )
    