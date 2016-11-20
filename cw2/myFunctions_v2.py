

MODULES = 4
STUDENTS = 7
students = ["Bob",
             "Sue",
             "Lou",
             "Stu",
             "Sam",
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
    [86 ,74, 64, 86],
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

def averageMarksByStudentNumber(studentNum, tableName):
    for i in range(STUDENTS):
        averageMarks=0
        for j in range(MODULES):
            averageMarks = averageMarks + tableName[studentNum][j]/MODULES
    return(int(averageMarks))

#tableName Version
def averageMarksByModuleNumber(moduleNum, tableName):
    for i in range(MODULES):
        averageModuleMarks=0
        for j in range(STUDENTS):
            averageModuleMarks = averageModuleMarks + tableName[j][moduleNum]/STUDENTS
    return(int(averageModuleMarks))

def findIndxOfNextMinValue(studentAverageList, listOfIndexesToExclude):
	minVal = -2 # initialising minVal to a large number (maxint), which can be imported from the library sys
	minIndx = 0		
	for i in range(len(studentAverageList)):
		if minVal <= studentAverageList[i] and (i not in listOfIndexesToExclude):
			minVal = studentAverageList[i]
			minIndx = i
	return minIndx

def sortList(studentAverageList):
	indxsOfSortedList = [] # this is the list that will hold the indexes of sorted A
	for a in studentAverageList:
		indxOfMinVal = findIndxOfNextMinValue(studentAverageList,indxsOfSortedList)
		indxsOfSortedList.append(indxOfMinVal)
	return indxsOfSortedList

#Original
#def averageMarksByModuleNumber(moduleNum):
#    for i in range(MODULES):
#        averageModuleMarks=0
#        for j in range(STUDENTS):
#            averageModuleMarks = averageModuleMarks + (marks[j][moduleNum])/STUDENTS
#    return(int(averageModuleMarks))

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
