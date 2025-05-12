start = int(input("Starting number: "))
end = int(input("Ending number: "))
evenorodd=input("Even or Odd?: ")

print("Starting number: ",start)
print("Ending number: ",end)
print("Even or Odd?: ", evenorodd)
for i in range(start,end+1):
    if evenorodd == "even" and i % 2 == 0:
        print(i)
    if evenorodd == "odd" and i % 2 != 0:
        print(i)
numstudents = int(input('students: '))

# ask the teacher for assignments
numassignments = int(input('assignments: '))

# go through each student
for student in range(0,numstudents):

	print("Student #", student+1)
	
	# assume the student earned no points
	studentpoints = 0

	# go through each assignment
	for assignment in range(0,numassignments):

		# get points earned for this assignment
		score = float(input('Assignment: ' + str(assignment+1) ))
		
		# add to this student's points
		studentpoints += score
        
	# loop is over - compute student's score
	print("This student earned:", studentpoints/numassignments)
