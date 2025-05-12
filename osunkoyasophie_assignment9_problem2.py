# function:   valid_username
# input:      a username (string)
# processing: determines if the username supplied is valid.  for the purpose
#             of this program a valid username is defined as follows:
#             (1) must be 5 characters or longer
#             (2) must be alphanumeric (only letters or numbers)
#             (3) the first character cannot be a number
# output:     boolean (True if valid, False if invalid)

def valid_username(string):
	valid = False
	if len(string) >= 5:
		if string.isalnum() and string[0].isalpha():
			valid = True

	return valid	

# function:   valid_password
# input:      a password (string)
# processing: determines if the password supplied is valid.  for the purpose
#             of this program a valid password is defined as follows:
#             (1) must be 5 characters or longer
#             (2) must be alphanumeric (only letters or numbers)
#             (3) must contain at least one lowercase letter
#             (4) must contain at least one uppercase letter
#             (5) must contain at least one number
# output:     boolean (True if valid, False if invalid)

def valid_password(string):
	Lower = 'abcdefghijklmnopqrstuvwxyz'
	Upper = Lower.upper()
	low = up = dig = 0
	valid = False
	if len(string) >= 5 and string.isalnum():
		for i in string:
			if i in Lower:
				low = 1
			if i in Upper:
				up = 1
			if i.isdigit():
				dig = 1	
			if low+up+dig == 3:
				valid = True
				break
	
	return valid


# function:   username_exists
# input:      a username (string)
# processing: determines if the username exists in the file 'user_info.txt'
# output:     boolean (True if found, False if not found)
#determines if the username exists in the file 'user_info.txt'
def username_exists(username):
        exists = False
        file = open('user_info.txt','r')
        for values in file:
            if len(values)>1:
                
                user,password1 =(values.strip().split(','))
                if(user == username):
                        exists = True
                        break
        file.close()
        return exists           

# function:   check_password
# input:      a username (string) and a password (string)
# processing: determines if the username / password combination
#             supplied matches one of the user accounts represented
#             in the 'user_info.txt' file
# output:     boolean (True if valid, False if invalid)

def check_password(username,password):
        match = False
        file = open('user_info.txt','r')
        for values in file:
             if len(values)>1:
                user,password1 = values.strip().split(',')
                if(user == username and password1 == password):
                        match = True
                        break
        file.close()
        return match

# function:   add_user
# input:      a username (string) and a password (string)
# processing: if the user being supplied is not already in the
#             'user_info.txt' file they should be added, along with
#             their password.
# output:     boolean (True if added successfully, False if not)

def add_user(username, password):
        success = False
        if(not username_exists(username)):
                with open('user_info.txt','a') as file:
                        file.write('\n'+username+','+password)
                
                send_message('admin',username,'Welcome to your account!')
                success = True  
        
        return success  
    

# function:   send_message
# input:      a sender (string), a recipient (string) and a message (string)
# processing: writes a new line into the specific messages file for the given users
#             with the following information:
#
#             sender|date_and_time|message\n
#
#             for example, if you call this function using the following arguments:
#
#             send_message('craig', 'pikachu', 'Hello there! nice to see you!')
#
#             the file 'messages/pikachu.txt' should gain an additional line data
#             that looks like the following:
#
#             craig|11/14/2020 12:30:05|Hello there! nice to see you!\n
#
#             note that you can generate the current time by doing the following:
#
#             import datetime
#             d = datetime.datetime.now()
#             month = d.month
#             day = d.day
#             year = d.year
#             ... etc. for hour, minute and second
#
#             keep in mind that you may need to 'append' to the correct messages file
#             since a user can receive an unlimited number of messages.  you may also
#             need to create

import datetime

def send_message(sender, recipient, message):
	d = datetime.datetime.now()
	dateTime = str(d)[:-7].replace('-','/')
	message_data = '|'.join([sender,dateTime,message+'\n'])
	if(username_exists(recipient)):
		with open('messages/'+recipient+'.txt','a') as file:
			file.write(message_data)
	else:
		with open('messages/newMessage.txt','a') as file:
			file.write(message_data)
			


# function:   print_messages
# input:      a username (string)
# processing: prints all messages sent to the username in question.  assume you have this file named 'pikachu.txt':
#
#             charmander|11/14/2020 13:37:15|Hey there!
#             charmander|11/14/2020 13:37:15|You too, ttyl
#
#             this function should generate the following output:
#
#             Message #1 received from charmander
#             Time: 11/14/2020 13:37:15
#             Hey there!
#
#             Message #2 received from charmander
#             Time: 11/14/2020 13:37:15
#             You too, ttyl
# output:     no return value (simply prints the messages)

def print_messages(username):
        if(not username_exists(username)):
            return
        with open('messages/'+username+'.txt','r') as file:
                count = 1
                check=file.read()
                
                if check=='':
                    print('No messages in your inbox')
                else:
                    for info in check.split("\n"):
                        if(len(info)<=1):
                            break
                        #print(info)
                        name,time,message = info.strip().split('|')
                        print("Message #{} received from {}".format(count,name))
                        print("Time:",time)
                        print(message)
                        print()
                        count += 1
                       
# function:   delete_messages
# input:      a username (string)
# processing: erases all data in the messages file for this user
# output:     no return value

def delete_messages(username):
        #if username does not exists, it will do nothing
        if(not username_exists(username)):
                return
        #override previous file with a blank file
        with open('messages/'+username+'.txt','w'):
            pass



def main():
    #loop for login, register, quit
    while True:
        #prompting user 
        userChoice = input("(l)ogin, (r)egister or (q)uit: ").lower()
        
        # if condition to login
        if userChoice == 'l':
            print("Log in")
            #prompting user 
            usrName = input("Username (Case sensitive): ")
            password = input("Password (Case sensitive): ")
            
            # validating user name and password if correct then login
            if check_password(usrName, password):
                
                
                #loop when logged in successfully
                while True:
                    print("You have been logged in succesfully as",usrName)
                    #prompting user to select  
                    actionChoice = input("Please choose the action: (R)ead messages (S)end messages (D)elete messages (L)og out :").lower()
                    
                    # if condition to read messages
                    if actionChoice=='r':
                        print('reading')
                        print_messages(usrName) 
                    
                    # if condition to send message
                    elif actionChoice=='s':
                        
                        
                        #prompting user to enter recipient user name and message to be sent 
                        recipientUsrname = input("Username of recipient: ")
                        if username_exists(recipientUsrname):
                            msg = input("Type your message here: ")
                        
                       
                            send_message(usrName,recipientUsrname, msg)

                            print("Message sent!")
                        else:
                            print("unknown recipient")
                            continue
                    # if condition to delete messages
                    elif actionChoice=='d':
                        print("Your messages have been deleted")
                        
                        #calling delete_messages function
                        delete_messages(usrName)
                        
                    # if condition to log out and break the loop
                    elif actionChoice=='l':
                        print("Logging out as username",usrName)
                        break
                        
                    # if user enters any other input
                    else:
                        print("Wrong choice.")
                        
            
            else:
                print("Invalid user name or password.")
            
        #if condition to register action
        elif userChoice == 'r':
            print("Register for an account ")
            

            usrName = input("Username (Case sensitive): ")
            password = input("Password (Case sensitive): ")
            
            #validating user name and password
            if valid_password(password) and valid_username(usrName):
                
                #checking whether user already exist
                if add_user(usrName, password):
                    print("Registration successful!")
                else: 
                    print("Duplicate username, registration cancelled")
                    
            else:
                print("Password is invalid, registration cancelled")
                
        # condition to quit and break the loop
        elif userChoice == 'q':
            print("Goodbye!")
            break
        
        #if any other input 
        else:
            print("You entered wrong choice.")
        
# call the main function
main()
                
            


