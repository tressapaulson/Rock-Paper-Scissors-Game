import random

print("Made by Tressa Poulose")

def rules():
    print("Rules")
    print("")
    print("Rock beats scissors")
    print("Rock looses to paper")
    print("Paper beats rock")
    print("Paper looses to scissors")
    print("Scissors beats paper")
    print("Scissors looses to rock")

while True:
    loose = ("Computer Wins")
    win = ("You win")
    lives = 5
    score = 0
    draw = 0
    computer_lives = 5
    print("-----------------------------")
    print("ROCK PAPER SCISSORS")
    print("-----------------------------")
    print("Live rules")
    print("You start with ",lives," lives")
    print("If you win you will score else you will loose a life")
    print("Computer too has lives")
    print("If you want to read the rules again type rules")
    print("If you want to exit the game type exit")
    print("Make sure you don't use capital letters")
    print("Do you think you will be able to beat the computer???")
    print("Good Luck!!!")
    while True:
        rps = input("rock, paper, scissors?    ")
        computer = ('rock','paper','scissors')
        computer = random.choice(computer)
        #rock if statement
        if rps == "rock" and computer == "paper":
            print("Choice of computer is: " +computer)
            print(loose)
            print("")
            lives-=1
        if rps == "rock" and computer == "scisscors":
            print("Choice of computer is: " +computer)
            print(win)
            print("")
            computer_lives-=1
            score+=1
        #paper if statement
        if rps == "paper" and computer == "scissors":
            print("Choice of computer is: " +computer)
            print(loose)
            print("")
            lives-=1
        if rps == "paper" and computer == "rock":
            print("Choice of computer is: " +computer)
            print(win)
            print("")
            computer_lives-=1
            score+=1
        #scissors if statement
        if rps == "scissors" and computer == "rock":
            print("Choice of computer is: " +computer)
            print(loose)
            print("")
            lives-=1
        if rps == "scissors" and computer == "paper":
            print("Choice of computer is: " +computer)
            print(win)
            print("")
            computer_lives-=1
            score+=1
        #duplicates
        if rps == "rock" and computer == "rock":
            print("Choice of computer is: " +computer)
            print("Draw")
            print("")
            draw+=1
        if rps == "paper" and computer == "paper":
            print("Choice of computer is: " +computer)
            print("Draw")
            print("")
            draw+=1
        if rps == "scissors" and computer == "scissors":
            print("Choice of computer is: " +computer)
            print("Draw")
            print("")
            draw+=1
        #System
        if rps == "rules":
            rules()
        if rps == "lives":
            print(lives)
        if rps == "draw":
            print(draw)
        if rps == "score":
            print(score)
        #lives
        if lives == 0 or rps=="test":
            print("You ran out of lives ")
            print("You got ",score," score")
            print("You draw ",draw," times")
            stop = input("Press Enter to exit")
            exit()
        if computer_lives == 0 :
            print("Computer ran out of lives ")
            print("You got ",score," score")
            print("You draw ",draw," times")
            stop = input("Press Enter to exit")
            exit()
        #exit
        if rps == "exit":
            break
    if rps == "exit":
        option = input("Do you want to play another game?(y/s)   ")
        if option == 'y':
            break