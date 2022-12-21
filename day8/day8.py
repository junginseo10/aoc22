from pathlib import Path
from collections import deque
import time
import re
import numpy as np


SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

def main():
    
    
    ### PART I ###
    with open(INPUT_FILE, mode='rt') as f:        
        map = f.read()
        map_matrix = parse(map)
        r,c = map_matrix.shape
        
        sum = r*c - (r-2)*(c-2)
        
        for i in range(1,c-1):
            for j in range(1, r-1):
                sum += is_visible(map_matrix, i, j)
        
        print(f"{sum} units are visible.")
    
    
    ### PART II ###
    with open(INPUT_FILE, mode='rt') as f:        
        map = f.read()
        map_matrix = parse(map)
        r,c = map_matrix.shape
        
        score = 0
        
        #scenic_score(map_matrix, 3, 2)
        
        for i in range(1,c-1):
            for j in range(1, r-1):
                score = max(scenic_score(map_matrix, i, j), score)

        print(f"The highest score is {score}")
    
def parse(input):
    strings = input.strip().split("\n")
    return np.array([[int(c) for c in list(s)] for s in strings])

def is_visible(map, i, j):
    r, c = map.shape
    curr_height = map[i,j]
    
    t = map[0:i, j:j+1]
    b = map[i+1:r, j:j+1]
    l = map[i:i+1, 0:j]
    r = map[i:i+1, j+1:c]
    
    l = curr_height > l.max()
    t = curr_height > t.max()
    r = curr_height > r.max()
    b = curr_height > b.max()
    
    return l or t or r or b

def scenic_score(map, i, j):

    r, c = map.shape
    curr = map[i,j]
    
    u = np.flip(map[0:i, j:j+1], axis=0)
    b = map[i+1:r, j:j+1]
    l = np.flip(map[i:i+1, 0:j], axis= 1)
    r = map[i:i+1, j+1:c]
    
    s = ["up", "left", "right", "bottom"]
    score = [0,0,0,0]
    
    for i, dir in enumerate([u,l,r,b]):
        dir_list = dir.flatten().tolist()
        for j, num in enumerate(dir_list):
            if num >= curr:
                score[i] = j+1
                break
            elif j == len(dir_list)-1:
                score[i] = len(dir_list)
            else:
                pass
    
    # print(f"scores are: {score}, total: {np.prod(score)}")
    return np.prod(score)
       
if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2-t1:0.4f} seconds" )
    