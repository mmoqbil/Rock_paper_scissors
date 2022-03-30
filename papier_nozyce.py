import random
def check_who_won(player,computer):
    if player == computer:
        print("You lose",player,"a komputer",computer)
    elif (player=="Scissor") and (computer=="Sock"):
        print("computer wins")

    elif player == ("Rock") and (computer=="Paper"):
        print("You lost!")
    elif (player == "Rock") and (computer == "Scissors"):
        print ("You win!")
    elif  (player =="Paper") and (computer =="Rock"):
        print ("You win!")
    elif (player == "Paper") and (computer =="Scissors"):
        print ("You lost!")
    elif (player =="Scissors") and (computer =="Rock"):
        print ("You lose!")
    elif (player =="Scissors") and (computer == "Paper"):
        print ("You win")
choices = ["Rock","Paper","Scissors"]
computer = random.choice(choices)
print("Wellcome to Play 'Rock, Paper or Scissors'")
your_choice=input("Choose: Rock, Paper or Scissors (letter size matter): ")
while (your_choice!="Rock") and (your_choice!="Paper") and (your_choice!="Scissors"):
    print("Wrong word")
    your_choice=input("Play again ")


print(computer)
check_who_won(your_choice,computer)



