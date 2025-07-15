#Joe Melia EET-107

def main():
    print("State Capital's Game\n")
    states = {"Ohio":"Columbus","Michigan":"Lansing","Indiana":"Indianapolis","Illinois":"Springfield","West Virginia":"Charleston"}
    correct = 0
    incorrect = 0
    for state, capital in states.items():
        game = input(f"What is the capital of {state}?\nType your answer: ")
        if game == capital:
            print("\nGood Job\n")
            correct += 1
        else:
            print(f"\nSorry the answer is {capital}\n")
            incorrect += 1
    print(f"You answered {correct} correctly, and {incorrect} incorrectly.")
main()
