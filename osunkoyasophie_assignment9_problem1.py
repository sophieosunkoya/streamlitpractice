print ("NYU Computer Science Registration System")
courses = {}
enrollment = {}
with open ("class_data.txt") as f:
    for x in f:
        line = x.strip().split(',')
        courses[line[0]] = line[1]

with open ("enrollment_data.txt") as f:
    for x in f:
        line = x.strip().split(',')
        if line[0] in enrollment:
            enrollment[line[0]].append (line[1] + "," + line[2])
        else:
            enrollment[line[0]] = [line[1] + "," + line[2]]

course1 = ""
while course1 not in courses:
    course1 = input ("Enter a course ID (i.e. CS0002, CS0004): ")
    if course1 not in courses:
        print ("Cannot find this course")

print ("The title of this class is:", courses[course1])
if course1 in enrollment:
    count1 = len (enrollment[course1])
else:
    count1 = 0
print ("The course has {} students enrolled".format (count1))
if count1 > 0:
    for student in enrollment[course1]:
        print ("*", student)
