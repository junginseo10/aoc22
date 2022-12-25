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
    
    
    ### PART I ###
    with open(INPUT_FILE, mode='rt') as f:  
        rounds = 20
        monkeys = []    
        monkey_strings = f.read().strip().split("\n\n")
        for monkey_string in monkey_strings:
            monkeys.append(parse(monkey_string))
        
        for m in monkeys:
            print(f"    Monkey {m.name}: {m.items}")
            m.show_details()
            
        print(monkeys[2].test(1))
        print(monkeys[2].test(6241))
            
        for r in range(rounds):
            print(f"ROUND {r+1}:")
            for m in monkeys:
                # print(f"  Current Monkey: {m.name}")
                m.throw()
                        
        inspected = []
        for m in monkeys:
            print(m)
            inspected.append(m.get_inspected())
            
        print(f"Monkey Business level: {np.prod(sorted(inspected, reverse = True)[:2])}")
            
            
        
def create_divisor(operand, operator, test):
    if operand == 'old':
        operand = 'x'
        
    def f(x):
        return eval(operand) 
def create_operation(operand, operator):
    if operand == 'old':
        operand = 'x'
        
    def f(x):
        return eval('x' + operator + operand)
    
        
    return f

def parse(monkey_string):
    lines = monkey_string.split("\n")
    name = re.findall("(\d+)", lines[0])[0]
    starting_items = [int(x) for x in re.findall("(\d+)", lines[1])]
    operator, operand = re.findall("(\+|\*)\s(old|\d+)", lines[2])[0]
    test = int(re.findall("(\d+)", lines[3])[0])
    true_throw = re.findall("(\d+)", lines[4])[0]
    false_throw = re.findall("(\d+)", lines[5])[0]
    return Monkey(name, starting_items, create_operation(operand, operator), lambda x: x % test == 0, create_divisor(operator, operand, test), true_throw, false_throw)
       

class Monkey:
    
    _active = {}
    
    
    def __init__(self, name, starting_items, operation, test, div, true_throw, false_throw):
        self.name = name
        self.items = deque(starting_items)
        self.operation = operation
        self.test = test
        self.div = div
        self.true_throw = true_throw
        self.false_throw = false_throw
        self.inspected = 0
        Monkey._active[name] = self
        
    def __str__(self):
        return f"Monkey {self.name}:\n  items: {self.items}\n  inspected items {self.inspected} times."
    
    def show_details(self):
        print(f"Monkey {self.name}:\n  items: {self.items}\n  inspected items {self.inspected} times.")
        print(f"  Throw to: {self.true_throw} or {self.false_throw}")
        print(f"  Using the first item {self.items[0]}, the operation will result in: {self.operation(self.items[0])}")
        print(f"  Using the result {self.operation(self.items[0])}, the test will result in: {self.test(self.operation(self.items[0]))}")
        
    def throw(self):
        self.check_throw()
        while len(self.items) > 0:
            item = self.items.popleft()
            item_to_test = self.operation(item)
            self.inspected += 1
            item_to_throw = item_to_test
            if self.test(item_to_throw):
                comm_divisor = self.div(item) * self.true_throw.div(item)
                self.true_throw.receive(item_to_throw % comm_divisor)
            else:
                comm_divisor = self.div(item) * self.false_throw.div(item)
                self.false_throw.receive(item_to_throw % comm_divisor)
    
    def receive(self, item):
        self.items.append(item)
    
    def get_inspected(self):
        return self.inspected
    
    def check_throw(self):
        if type(self.true_throw) == str:
            self.true_throw = Monkey._active[self.true_throw]
        if type(self.false_throw) == str:
            self.false_throw = Monkey._active[self.false_throw]
    
    
            

    
if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2-t1:0.4f} seconds" )
    