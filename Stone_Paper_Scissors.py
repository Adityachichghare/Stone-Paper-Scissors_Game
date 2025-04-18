import random

print("Welcome to Stone, Paper, Scissors Game!")
print("Choose any one:")
print("1 = Stone")
print("2 = Paper")
print("3 = Scissors")

try:
    user = int(input("Your choice (1-3): "))
    if user not in [1, 2, 3]:
        print("Invalid input! Please choose 1, 2, or 3.")
    else:
        choices = {1: "STONE", 2: "PAPER", 3: "SCISSORS"}
        computer = random.randint(1, 3)

        print(f"You: {choices[user]}")
        print(f"Computer: {choices[computer]}")

        if user == computer:
            print("MATCH DRAW!")
        elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
            print("Congratulations, You Win!")
        else:
            print("Oops! You Lose")
except ValueError:
    print("Invalid input! Please enter a number.")
