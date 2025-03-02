# Rock-Paper-Scissors
import random

print("Welcome to Rock-Paper-Scissors!")

choices = ["rock", "paper", "scissors"]

while True:
    userchoice = input("\nEnter Rock, Paper or Scissors: ").strip().lower()

    if userchoice not in choices:
        print("Invalid choice, try again")
        continue  

    compchoice = random.choice(choices)
    print("Computer picked:", compchoice)

    if userchoice == "rock":
        if compchoice == "scissors":
            print("You win")
        elif compchoice == "paper":
            print("You lose")
        else:
            print("It's a tie")

    elif userchoice == "paper":
        if compchoice == "rock":
            print("You win")
        elif compchoice == "scissors":
            print("You lose")
        else:
            print("It's a tie")

    elif userchoice == "scissors":
        if compchoice == "paper":
            print("You win")
        elif compchoice == "rock":
            print("You lose")
        else:
            print("It's a tie")
            
        break
