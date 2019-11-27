import random

start = True
while(start): 
    i = random.randint(1,30)
    chances = 3
    while(chances != 0):
        num = int(input("Guess the Number Between (1 - 30) :- "))
        if (num == i):
            print("You Guessed Correct Number")
            chances = 0
        elif (num > i):
            print("You Entered Greater number")
            chances = chances - 1
        elif (num < i):
            print("You Entered Smaller number")
            chances = chances - 1
    
    print("Random Number is :- ",i)
    choice = str(input("Enter Y/y to Play Game again or N/n to Quit Game :- "))
    if(choice == "Y" or choice == "y"):
        start = True
    elif(choice == "N" or choice == "n"):
        start = False
    else:
        print("You Entered Wrong Choice so Game will be begun again ☻")
        start = True
