def main():

    print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!\n")
    
    attempt = 0
    guess = 100
    response = 17

    while 1:
        guess = input("What's your guess between 1 and 99?\n>> ")
        attempt += 1

        if guess == "exit":
            return
        elif guess.isdigit() == False:
            print("It is not a number")
        elif int(guess) == response:
            print("Congratulations, you've got it!\nYou won in " + str(attempt ) +  " attempts!")
            return
        elif int(guess) > response:
            print("Too hight!")
        elif int(guess) < response:
            print("Too low!")

if __name__=="__main__":
    main()
