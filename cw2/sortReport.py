import sys
import myFunctions_v2
from myFunctions_v2 import students
from myFunctions_v2 import modules
from myFunctions_v2 import STUDENTS
from myFunctions_v2 import MODULES
from myFunctions_v2 import averageMarksByStudentNumber
from myFunctions_v2 import averageMarksByModuleNumber
from myFunctions_v2 import averageMarksByStudentName
from myFunctions_v2 import averageMarksByModuleName

marks =[
    [42 ,65, 67, 78],
    [94 ,67, 56, 89],
    [72 ,88, 94, 97],
    [86 ,74, 64, 86],
    [99 ,86, 73, 75],
    [85 ,55, 82, 98],
    [54 ,44, 91, 82]
   ]

#def findIndxOfNextMinValue(studentAverageList, listOfIndexesToExclude):
#	minVal = sys.maxsize # initialising minVal to a large number (maxint), which can be imported from the library sys
#	minIndx = 0		
#	for i in range(len(studentAverageList)):
#		if minVal >= studentAverageList[i] and (i not in listOfIndexesToExclude):
#			minVal = studentAverageList[i]
#			minIndx = i
#	return minIndx

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

studentAverageList=[]
for i in range(STUDENTS):
#    print(print(averageMarksByStudentNumber(i, tableName=marks)))
    studentAverageList.append(averageMarksByStudentNumber(i, tableName=marks))
print(studentAverageList)


                             
# print the sorted list A
for j in sortList(studentAverageList):
	print(studentAverageList[j], end=" ") # if you are using python 3, change this line to 'print(A[j], end=" ")'


print('') # print an empty line. if you're using Python 3 then change to 'print('')'

# print the list A, which has not been changed.
for a in studentAverageList:
	print(a, end=" ") # if you are using python 3, change this line to 'print(a, end=" ")'
print()

sortedList=[]
#for i in range(STUDENTS):
#    sortedList.append(sortList(studentAverageList))
#print(sortedList)

for j in sortList(studentAverageList):
    sortedList.append(studentAverageList[j])
print(sortedList)

for i in range(STUDENTS):
    print("Student Name", " ", "Average for the registered modules")
    for i in range(STUDENTS):    
        print(students[i], "           ", sortedList[i])
