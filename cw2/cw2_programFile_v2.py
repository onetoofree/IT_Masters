from myFunctions import averageMarksByStudentNumber
from myFunctions import averageMarksByModuleNumber
from myFunctions import averageMarksByStudentName
from myFunctions import averageMarksByModuleName

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

print("        Student          Maths      Art      French      Science       Total")

for i in range(STUDENTS):
    print("%15s" % students[i], end="")

    total=0
    for j in range(MODULES):
        print("%12d" % marks[i][j], end="")
        total = total + (marks[i][j]) / MODULES

    print("%12d" % total)

print()

#2.1
studentNum=int(input("Enter a number representing the student you want the average mark for: "))
print(averageMarksByStudentNumber(studentNum))
for i in range(STUDENTS):
    averageMarks=0
    for j in range(MODULES):
        averageMarks = averageMarks + marks[studentNum][j]/MODULES
    return(int(averageMarks))


#2.2
moduleNum=int(input("Enter a number representing the module you want the average mark for: "))
print(averageMarksByModuleNumber(moduleNum))

#2.3
studentName=input("Enter the name of the student you want the average mark for: ")
print(averageMarksByStudentName(studentName))

#2.4
moduleName=input("Enter the name of the module you want the average mark for: ")
print(averageMarksByModuleName(moduleName))

#2.5
studentAverage=[]
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

#2.6
moduleAverage=[]
for i in range(MODULES):
    moduleAverageMarks=0
    for j in range(STUDENTS):
        moduleAverageMarks = moduleAverageMarks + (marks[j][i])/STUDENTS
    #print(int(averageMarks))
    moduleAverage.append(int(moduleAverageMarks))
#print(moduleAverage)
print("Module Name", " ", "Average for the registered modules")
for i in range(MODULES):
    print(modules[i], "            ", moduleAverage[i])

