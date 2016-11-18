MODULES = 4
STUDENTS = 7
students = ["Bob",
             "Sue",
             "Lou",
             "Stu",
             "Stan",
             "Pam",
             "Ann"]


marks =[
    [42 ,65, 67, 78],
    [94 ,67, 56, 89],
    [72 ,88, 55, 97],
    [86 ,77, 64, 86],
    [99 ,66, 73, 75],
    [85 ,55, 82, 98],
    [54 ,44, 91, 82]
]

print("        Student          Maths      Art      French      Science       Total")

for i in range(STUDENTS):
    print("%15s" % students[i], end="")

    total=0
    for j in range(MODULES):
        print("%12d" % marks[i][j], end="")
        total = total + (marks[i][j]) / MODULES

    print("%12d" % total)

print()
        

tableName=input("Enter the table name:  ")
studentNum=int(input("Enter a number representing the student you want the average mark for: "))
for i in range(STUDENTS):
    averageMarks=0
    for j in range(MODULES):
        averageMarks = averageMarks + (marks[studentNum][j])/MODULES
print(int(averageMarks))

tableName=input("Enter the table name:  ")
moduleNum=int(input("Enter a number representing the module you want the average mark for: "))
for i in range(MODULES):
    averageModuleMarks=0
    for j in range(STUDENTS):
        averageModuleMarks = averageModuleMarks + (marks[moduleNum][i])/STUDENTS
print(int(averageModuleMarks))

#Give a module's name - need to finish this off
for i in range(STUDENTS):
    averageMark=0
    studentName="Stu"
    if students[i]==studentName:
        for j in range(MODULES):
            averageMark = averageMark + (marks[i][j])/MODULES        
        print(int(averageMark))

for i in range(MODULES):
    averageMark=0
    moduleName="Art"
    if [i]==studentName:
        for j in range(MODULES):
            averageMark = averageMark + (marks[i][j])/MODULES        
        print(int(averageMark))       
        
