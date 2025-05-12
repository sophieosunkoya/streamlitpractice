def add_user(username, password):
	success = False
	if(not username_exists(username)):
		with open('user_info.txt','a') as file:
			file.write('\n'+username+','+password)

		success = True	
	
	return success

add_user('foobar', 'abcABC123')
add_user('barfoo', 'xyz123ABC')
add_user('foobar', 'aTest123')
