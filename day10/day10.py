from pathlib import Path
from collections import deque
import time
import re
import numpy as np
import math


SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

def main():
    
    """
    ### PART I ###
    with open(INPUT_FILE, mode='rt') as f:        
        signals = f.read().strip().split("\n")
        cd = CommDev()
        
        for i, signal in enumerate(signals):
            cd.parse_signal(signal)
        
        cd.get_significant_signals()
    """

    ### PART II ###
    with open(INPUT_FILE, mode='rt') as f:
        signals = f.read().strip().split("\n")
        cd = CommDev(signals, 40)
        
        while cd.signals:
            cd.next()
            print(cd)
        cd.display()            
            

       

class Signal:
    
    def __init__(self, type, displacement = 0):
        self.type = type
        if type == 'noop':
            self.execution_cycle = 1
        if type == 'addx':
            self.execution_cycle = 2
        self.expired = False
        self.displacement = displacement
    
    def process(self):
        if self.execution_cycle == 1:
            self.expired = True
            return self.displacement
        else:
            self.execution_cycle -= 1
            return 0
            
            
class CommDev:
    
    def __init__(self, signals, px_width):
        self.cycle = 0
        self.x = 1
        self.signals = deque(signals)
        self.curr_signal = None
        self.signal_strengths = []
        self.crt = np.full((6,40), ' ')
        self.px_width = px_width
        
    
    def __str__(self):
        return f"Device on cycle {self.cycle}: {self.r, self.c}, X value: {self.x}."
    
    def next(self):
        if (self.curr_signal == None) or self.curr_signal.expired == True:
            try:
                s, d = self.parse(self.signals.popleft())
            except IndexError:
                self.signals = None
                
            self.curr_signal = Signal(type = s, displacement = int(d))
        self.draw()
        self.x += self.curr_signal.process()
        self.cycle += 1
        
            
    def draw(self):
        self.r, self.c = self.cycle // self.px_width, self.cycle % self.px_width
        self.crt[self.r, self.c] = '#' if self.x - 1 <= self.c <= self.x + 1 else '.'
            
    def display(self):
        output = '\n'.join(''.join(x) for x in self.crt.tolist())
        print(output)      
    
    def parse(self, signal):
        try:
            s, d = signal.split(" ")
            return s, d
        except ValueError:
            return signal, 0 
            
  
    
if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2-t1:0.4f} seconds" )
    