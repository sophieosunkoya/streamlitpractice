while True:

	# ask the user to answer a math question
	answer = int(input("What is 2+2? "))
	
	# did they get it right?
	if answer == 4:
            print("Correct!")
            break
		
	# did they get it wrong?
	elif number!=4:
            print("Incorrect, try again")
            continue
