import random

print("Welcome to Rock-Paper-Scissors!")

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

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
            user_score += 1
        elif compchoice == "paper":
            print("You lose")
            computer_score += 1
        else:
            print("It's a tie")

    elif userchoice == "paper":
        if compchoice == "rock":
            print("You win")
            user_score += 1
        elif compchoice == "scissors":
            print("You lose")
            computer_score += 1
        else:
            print("It's a tie")

    elif userchoice == "scissors":
        if compchoice == "paper":
            print("You win")
            user_score += 1
        elif compchoice == "rock":
            print("You lose")
            computer_score += 1
        else:
            print("It's a tie")

    print(f"Score: You {user_score} - {computer_score} Computer")

    break

     
