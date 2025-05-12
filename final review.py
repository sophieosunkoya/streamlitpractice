tech_terms = { "dict": "stores a key/value pair",
               "list": "stores a value at each index",
               "map": "see 'dict'",
               "set": "stores unordered unique elements" }


def menu():
    ''' Print a simple menu to the user '''
    print("Systems Dictionary")
    print("1) Add a term")
    print("2) List terms")
    print("3) Get a definition")
    print("4) Delete a term")
    print("5) Quit")
    return input("Enter your choice: ")


def run(choice):
    ''' Runs one of the actions that the user choose.  Valid choices are:
        1-4 each of which corresponds to a specific action '''
    if choice == 1:
        add()
    elif choice == 2:
        list()
    elif choice == 3:
        lookup()
    elif choice == 4:
        delete()
    else:
        print("Invalid input, please enter a valid number (1-5)")


def add():
    ''' Adds a term to the dictionary '''
    # Get a new term and definition from the user
    term = input("What term do you want to add? ").lower()
    definition = input("What is the definition for '" + term + "'? ")

    # Add the term/definition from the user to the dictionary
    tech_terms[term]=definition
   


def list():
    ''' List all the terms (no definitions) that are in the dictionary.
        Once all terms have been listed, this function will also print
        the total number of entries in the dictionary '''
    # TODO: Add your code here
    for key in tech_terms.keys():
        print(keys)
print("Total number of entries is",len(tech_terms))


def lookup():
    ''' Lookup a term and print the definition '''
    # Get a term to lookup in the dictionary from the user
    term = input("What term do you want to lookup? ").lower()

    # Print the definition from for the term
    print(tech_terms[term])


def delete():
    ''' Deletes a term from the dictionary '''
    # Get a term to delete from the user
    term = input("What term do you want to delete? ")

    # Delete the term specified by the user from the dictionary
    del tech_terms[terms]


def main():
    ''' Keeps presenting the menu to the user till user asks to quit '''
    # Present main menu
    choice = menu()

    # While user hasn't asked to quit
    while choice != "5":
        try:
            # Run the code depending on user's choice
            choice = int(choice)
            run(choice)
        except:
            # User didn't enter a number
            print("Invalid input, please enter a valid number (1-5)")

        # Get next choice from user
        choice = menu()


# Run the program
main()

