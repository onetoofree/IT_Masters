MODULES = 4
STUDENTS = 7
students = ["Bob",
             "Sue",
             "Lou",
             "Stu",
             "Stan",
             "Pam",
             "Ann"]

modules = ["Maths",
           "Art",
           "French",
           "Science",]

marks =[
    [42 ,65, 67, 78],
    [94 ,67, 56, 89],
    [72 ,88, 94, 97],
    [86 ,77, 64, 86],
    [99 ,86, 73, 75],
    [85 ,55, 82, 98],
    [54 ,44, 91, 82]
]

studentAverage=[]
moduleAverage=[]

print("        Student          Maths      Art      French      Science       Total")

for i in range(STUDENTS):
    print("%15s" % students[i], end="")

    total=0
    for j in range(MODULES):
        print("%12d" % marks[i][j], end="")
        total = total + (marks[i][j]) / MODULES

    print("%12d" % total)

print()

for i in range(STUDENTS):
    studentAverageMarks=0
    for j in range(MODULES):
        studentAverageMarks = studentAverageMarks + (marks[i][j])/MODULES
    #print(int(averageMarks))
    studentAverage.append(int(studentAverageMarks))
#print(studentAverage)

print("Student Name", " ", "Average for the registered modules")
for i in range(STUDENTS):    
    print(students[i], "           ", studentAverage[i])

print()


for i in range(MODULES):
    moduleAverageMarks=0
    for j in range(STUDENTS):
        moduleAverageMarks = moduleAverageMarks + (marks[j][i])/STUDENTS
    #print(int(averageMarks))
    moduleAverage.append(int(moduleAverageMarks))
#print(moduleAverage)

for i in range(MODULES):
    print(modules[i], " ", moduleAverage[i])
