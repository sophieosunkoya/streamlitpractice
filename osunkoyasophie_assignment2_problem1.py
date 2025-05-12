#Sophie Osunkoya 9/15/22 CSCI-UA.0002-011 Python
#create variables that are inputs for assignments,quiz,midterm and desired grade
assignmentgrade=float(input("What was your grade on assignments? "))
quizgrade=float(input("What was your grade on quizzes? "))
midtermgrade=float(input("What was your grade on the midterm? "))
desiredgrade=float(input("What is your desired grade? "))
#set the final to the formula that creates a final exam score
final=((0.3*assignmentgrade+0.1*quizgrade+0.3*midtermgrade-desiredgrade)/-0.3)
final1="{:.2f}".format(final)
print()
#print the phrase along with the final score and desired grade
print("You need to receive a",final1,"on your final to get a",desiredgrade,"in the class.")
