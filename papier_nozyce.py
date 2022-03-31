import random
your_wins=0
computer_wins=0
play_again="Y"
def check_who_won(player,computer):
    global computer_wins
    global your_wins
    if player == computer:
        print("It's draw!")
    elif (player == "Rock") and (computer == "Paper"):
        print("You lose!")
        computer_wins += 1
    elif (player == "Rock") and (computer == "Scissors"):
        print("You win!")
        your_wins += 1
    elif (player=="Paper") and (computer == "Scissors"):
        print("You Lose!")
        computer_wins += 1
    elif (player == "Paper") and (computer == "Rock"):
        print("You win!")
        your_wins += 1
    elif (player=="Scissors") and (computer == "Rock"):
        print("You lose!")
        computer_wins+=1
    elif (player=="Scissors") and (computer == "Paper"):
        print("You win!")
        your_wins += 1
        
while (play_again == "Y"):
    choices = ["Rock","Paper","Scissors"]
    computer_choice = random.choice(choices)
    print("Wellcome into 'Rock, Paper or Scissors'")
    your_choice=input("Type: Rock, Paper or Scissors(Letter size matter): ")
    while (your_choice!="Rock") and (your_choice!="Paper") and (your_choice!="Scissors"):
        print("Wrong word")
        your_choice=input("Type again: ")
    print("Your choice:",your_choice)
    print("Computer:",computer_choice)
    check_who_won(your_choice,computer_choice)
    print("You won: ",your_wins,"times")
    print("Computer won: ",computer_wins,"times")
    play_again = input("Wanna play again? Y/N ")
    while (play_again != "Y" and play_again != "N"):
        play_again = input("Type Y to continue and N to quit!: ")
    