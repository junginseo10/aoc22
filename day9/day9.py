from pathlib import Path
from collections import deque
import time
import re
import numpy as np
import math


SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "sample_input.txt")
#INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

def main():
    
    """
    ### PART I ###
    with open(INPUT_FILE, mode='rt') as f:        
        commands = f.read().strip().split("\n")
        head = Head()
        tail = [Tail(head= head)]
        
        for i, command in enumerate(commands):
            parse(command, head, tail)
        
        tail[0].count_visited()
    """
    
    ### PART II ###
    with open(INPUT_FILE, mode='rt') as f:        
        commands = f.read().strip().split("\n")
        head = Head()
        tails = {}
        tail_count = 9
        
        for i in range(tail_count):
            tails[f"Tail {i+1}"] = Tail(name= f"Tail {i+1}")
            
        for i, k in enumerate(sorted(tails.keys())):
            if i == 0:
                tails[k].head = head
            else:
                tails[k].head = tails[f"Tail {i}"]
        
        for i, k in enumerate(sorted(tails.keys())):
            tails[k].show_head()
            
        for i, command in enumerate(commands):
            parse(command, head, tails)
        
        tails["Tail 9"].count_visited()
        
class Head:
    
    def __init__(self):
        self.coord = [0,0]
        self.visited = set()
        self.visited.add((0,0))
    
    def __str__(self):
        return f"Head located at ({self.coord})"
    
    def count_visited(self):
        print(f"Visited {len(self.visited)} positions so far.")
        
    def show_head(self):
        print(self.head)
    
    def move(self, dir):
        match dir:
            case "R":
                self.coord[0] += 1
            case "L":
                self.coord[0] -= 1
            case "U":
                self.coord[1] += 1
            case "D":
                self.coord[1] -= 1
        
        self.visited.add(tuple(self.coord))
            

class Tail(Head):
    
    def __init__(self, head=None, name=None):
        self.coord = [0,0]
        self.visited = set()
        self.visited.add((0,0))
        self.head = head
        self.name = name
        
    def __str__(self):
        return f"{self.name} located at ({self.coord})"


    def follow(self):
        head = self.head
        x_diff = head.coord[0] - self.coord[0]
        y_diff = head.coord[1] - self.coord[1]

        if abs(x_diff) > 1 or abs(y_diff) > 1:
            self.coord = [self.coord[0] + np.sign(x_diff), self.coord[1] + np.sign(y_diff)]

        self.visited.add(tuple(self.coord))
        
def parse(command, head, tails):
    dir, l = command.split(" ")
    # print(f"*Command: {command}")
    for j in range(eval(l)):
        # print(f"  **Subcommand: {dir} {j+1}")

        head.move(dir)
        for k in sorted(tails.keys()):
            tails[k].follow()
        # print(f"    {head}")
        # print(f"    {tail}")
        # print(f"    Head visited: {head.visited}")
        # print(f"    Tail visited: {tail.visited}")
        
    
if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2-t1:0.4f} seconds" )
    