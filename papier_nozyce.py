import random
your_wins=0
computer_wins=0
play_again="Y"
def check_who_won(player,computer):
    global computer_wins
    global your_wins
    if player == computer:
        print("Padł remis!")
    elif (player == "Rock") and (computer == "Paper"):
        print("Komputer wygrał!")
        computer_wins += 1
    elif (player == "Rock") and (computer == "Scissors"):
        print("Brawo! Wygrałeś!")
        your_wins += 1
    elif (player=="Paper") and (computer == "Scissors"):
        print("Komputer wygrał!")
        computer_wins += 1
    elif (player == "Paper") and (computer == "Rock"):
        print("Brawo! Wygrałeś!")
        your_wins += 1
    elif (player=="Scissors") and (computer == "Rock"):
        print("Komputer wygrał!")
        computer_wins+=1
    elif (player=="Scissors") and (computer == "Paper"):
        print("Brawo! Wygrałeś!")
        your_wins += 1
        
while (play_again == "Y"):
    choices = ["Rock","Paper","Scissors"]
    computer_choice = random.choice(choices)
    print("Witamy w grze 'Rock, Paper or Scissors")
    your_choice=input("Wpisz Rock, Paper albo Scissors(wielkość liter ma znaczenie): ")
    while (your_choice!="Rock") and (your_choice!="Paper") and (your_choice!="Scissors"):
        print("Wprowadziłeś zły kod")
        your_choice=input("Wpisz ponownie: ")
    print("Ty:",your_choice)
    print("Komputer:",computer_choice)
    check_who_won(your_choice,computer_choice)
    print("Wygrales",your_wins,"razy")
    print("Komputer wygral",computer_wins,"razy")
    play_again = input("Chcesz zagrać ponownie? Y-Tak, N-Nie: ")
    while (play_again != "Y" and play_again != "N"):
        play_again = input("Wprowadź Y gdy chcesz grać dalej i N gdy chcesz zakończyć!: ")
    