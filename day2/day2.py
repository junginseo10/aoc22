from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
#INPUT_FILE = Path(SCRIPT_DIR, "sample_input.txt")
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

def main():
    with open(INPUT_FILE, mode='rt') as f:
        rounds = f.read().split("\n") #split input data into elf meal blocks by empty lines
        total_score = 0
        
        for i, round in enumerate(rounds):
            print(f"Round {i+1}")
            o, m = parse(round)
            # total_score += score_calc(o,m) #part 1
            total_score += move_calc(o,m) #part 2
        
        print(f"Fianl score is {total_score}")
                


def parse(round):
    opponent, move = round.split(" ")
    return opponent, move
   
def score_calc(opponent, move):
    moves = ["X", "Y", "Z"] # X = rock, Y = paper, Z = scissors
    opponents = ["A", "B", "C"] # A = rock, B = paper, C = scissors
    verbatim = ["Rock", "Paper", "Scissors"]
    round_outcomes = ["Draw", "Your Win", "Your Loss"]
    
    round_outcome_index = moves.index(move)-opponents.index(opponent)
    round_outcome_scores = [3,6,0]
    round_outcome_score = round_outcome_scores[round_outcome_index]

    round_move_score = moves.index(move) + 1
    
    total_score = round_outcome_score + round_move_score
    
    # print(f"    your move is {verbatim[moves.index(move)]}")
    # print(f"    opponent's move is {verbatim[opponents.index(opponent)]}")
    # print(f"    round outcome is {round_outcomes[round_outcome_index]}")
    # print(f"    your round score is {round_move_score} + {round_outcome_score} = {total_score}")
     
    return total_score

def move_calc(opponent, outcome):
    opponents = ["A", "B", "C"] # A = rock, B = paper, C = scissors
    outcomes = ["X", "Y", "Z"] # X = lose, Y = draw, Z = win
    verbatim = ["Rock", "Paper", "Scissors"]
    outcome_verbatim = ["Lose", "Draw", "Win"]

    outcome_scores = [0,3,6]
    moves = [1,2,3]
    
    round_move_score = moves[(opponents.index(opponent)+outcomes.index(outcome)-1)%3]
    round_outcome_score = outcome_scores[outcomes.index(outcome)]
    total_score = round_move_score + round_outcome_score
    
    # print(f"    Opponent's move is {verbatim[opponents.index(opponent)]}")
    # print(f"    Desired Outcome is {outcome_verbatim[outcomes.index(outcome)]}")
    # print(f"    You chose {verbatim[(opponents.index(opponent)+outcomes.index(outcome)-1)%3]}")
    # print(f"    Your Round Score is {round_move_score} + {round_outcome_score} = {total_score}")

    return total_score

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2-t1:0.4f} seconds" )
    