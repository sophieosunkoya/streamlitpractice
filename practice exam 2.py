for i in "BUTTER":
    while True:
        guess = input("Guess a letter: " )
        if guess == i:
            print("You got it! Moving onto the next.")
            
        else:
            print("Sorry, keep guessing.")
        
    print("Congrats, you guessed the word!")
    break
