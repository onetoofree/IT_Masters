#from myFunctions import averageMarksByStudentNumber

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
tableName=input("Enter the table name:  ")
studentNum=int(input("Enter a number representing the student you want the average mark for: "))
for i in range(STUDENTS):
    averageMarks=0
    for j in range(MODULES):
        table=tableName
        averageMarks = averageMarks + marks[studentNum][j]/MODULES
print(int(averageMarks))

#print(averageMarksByStudentNumber(3))

#2.2
tableName=input("Enter the table name:  ")
moduleNum=int(input("Enter a number representing the module you want the average mark for: "))
for i in range(MODULES):
    averageModuleMarks=0
    for j in range(STUDENTS):
        averageModuleMarks = averageModuleMarks + (marks[j][moduleNum])/STUDENTS
print(int(averageModuleMarks))
print()

#2.3
for i in range(STUDENTS):
    averageMark=0
    studentName="Bob"
    if students[i]==studentName:
        for j in range(MODULES):
            averageMark = averageMark + (marks[i][j])/MODULES        
        print(int(averageMark))

#2.4
for i in range(MODULES):
    averageMark=0
    moduleName="Science"
    if modules[i]==moduleName:
        for j in range(STUDENTS):
            averageMark = averageMark + (marks[j][i])/STUDENTS        
        print(int(averageMark))       
        
#2.5

