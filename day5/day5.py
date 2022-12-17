from pathlib import Path
import time
import re

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

def main():
    
    ### PART I ###
    with open(INPUT_FILE, mode='rt') as f:        
        init, moves = f.read().split("\n\n") # split the input text into initial state and move lines
        
        parse_init(init)
        
        Stack.show_all_stacks()
        
        for i, move in enumerate(moves.split("\n")):
            #print(f"Move #{i+1} is: {move}")
            num_moves, from_id, to_id = parse_move(move)
            Stack.move_stack(num_moves, from_id, to_id)
            #Stack.show_all_stacks()
        
        Stack.list_top_stacks()

    ### PART II ###
    with open(INPUT_FILE, mode='rt') as f:        
        init, moves = f.read().split("\n\n") # split the input text into initial state and move lines
        
        parse_init(init)
        
        Stack.show_all_stacks()
        
        for i, move in enumerate(moves.split("\n")):
            print(f"Move #{i+1} is: {move}")
            num_moves, from_id, to_id = parse_move(move)
            Stack.move_multiple_stacks(num_moves, from_id, to_id)
            #Stack.show_all_stacks()
        
        Stack.list_top_stacks()

def parse_move(str):
    # RegEx the input string into indices of the two list.
    num_moves, from_id, to_id = map(int, re.match(r"move (\d+) from (\d+) to (\d+)", str).groups())
    return num_moves, from_id, to_id

def parse_init(str):
    lines = str.split("\n")
    lines.reverse()
    indices = lines[0]
    stacks_config = lines[1:]
    
    for i, c in enumerate(indices):
        if c != ' ':
            id = int(c)
            crates = []
            for j in range(len(stacks_config)):
                if stacks_config[j][i] != ' ':
                    crates.append(stacks_config[j][i])
            Stack(id, crates)
                
    
    
class Stack:
    
    _instances = {}
    
    def __init__(self, id, crates):
        if not crates:
            self.crates = []
        self.id = id
        self.crates = crates
        self._instances[id] = self
    
    def load(self, item):
        self.crates.append(item)
        
    def load_multiple(self, items):
        self.crates.extend(items)
    
    def unload(self):
        return self.crates.pop()
    
    def unload_multiple(self, num):
        unloaded = self.crates[-num:]
        self.crates = self.crates[:-num]
        return unloaded
        
    
    def get_top_stack(self):
        return self.crates[-1]
    
    def show_stacks(self):
        output = [str(self.id)] +self.crates
        
        print(' '.join(output))
    
    @classmethod    
    def list_top_stacks(cls):
        top_stacks = ''
        ids = sorted(cls._instances)
        for id in ids:
            top_stacks += cls._instances[id].get_top_stack()
        print(top_stacks)
    
    @classmethod
    def move_stack(cls, num_moves, id_from, id_to):
        for move in range(num_moves):
            item = cls._instances[id_from].unload()
            cls._instances[id_to].load(item)
    
    @classmethod
    def move_multiple_stacks(cls, num_moves, id_from, id_to):
            items = cls._instances[id_from].unload_multiple(num_moves)
            cls._instances[id_to].load_multiple(items)
            
    @classmethod
    def show_all_stacks(cls):
        ids= sorted(cls._instances)
        for id in ids:
            cls._instances[id].show_stacks()
            
    


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2-t1:0.4f} seconds" )
    