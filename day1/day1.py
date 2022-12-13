from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

def main():
    with open(INPUT_FILE, mode='rt') as f:
        elf_meals = f.read().split("\n\n") #split input data into elf meal blocks by empty lines
    
    elf_calories = [] # list of total calories for each elf
    
    for meals in elf_meals:
        calories = sum(map(int, meals.splitlines()))
        elf_calories.append(calories)
        
    print(f"Part 1: {max(elf_calories)}")
    
    print(f"Part 2: {sum(sorted(elf_calories)[-3:])}")
    
if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2-t1:0.4f} seconds" )
    