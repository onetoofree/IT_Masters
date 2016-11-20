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

def averageMarksByStudentNumber(studentNum):
    for i in range(STUDENTS):
        averageMarks=0
        if students[i]==students[studentNum]:
            for j in range(MODULES):
                averageMarks = averageMarks + marks[studentNum][j]/MODULES
            return(int(averageMarks))

def averageMarksByModuleNumber(moduleNum):
    for i in range(MODULES):
        averageModuleMarks=0
        if modules[i]==modules[moduleNum]:
            for j in range(STUDENTS):
                averageModuleMarks = averageModuleMarks + (marks[moduleNum][i])/STUDENTS
            return(int(averageModuleMarks))

def averageMarksByStudentName(studentName):
    for i in range(STUDENTS):
        averageMark=0
        if students[i]==studentName:
            for j in range(MODULES):
                averageMark = averageMark + (marks[i][j])/MODULES        
            return(int(averageMark))


def averageMarksByModuleName(moduleName):
    for i in range(MODULES):
        averageMark=0
        if modules[i]==moduleName:
            for j in range(STUDENTS):
                averageMark = averageMark + (marks[j][i])/STUDENTS        
            return(int(averageMark))       
