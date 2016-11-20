import myFunctions_v2
import operator
from myFunctions_v2 import students
from myFunctions_v2 import modules
from myFunctions_v2 import STUDENTS
from myFunctions_v2 import MODULES
from myFunctions_v2 import averageMarksByStudentNumber
from myFunctions_v2 import averageMarksByModuleNumber
from myFunctions_v2 import averageMarksByStudentName
from myFunctions_v2 import averageMarksByModuleName
from myFunctions_v2 import findIndxOfNextMinValue
from myFunctions_v2 import sortList

marks =[
    [42 ,65, 67, 78],
    [94 ,67, 56, 89],
    [72 ,88, 94, 97],
    [86 ,74, 64, 86],
    [99 ,86, 73, 75],
    [85 ,55, 82, 98],
    [54 ,44, 91, 82]
]

marksss =[
    [42 ,65, 67, 99],
    [94 ,67, 56, 99],
    [72 ,88, 94, 99],
    [86 ,74, 64, 99],
    [99 ,86, 73, 99],
    [85 ,55, 82, 99],
    [54 ,44, 91, 99]
]

programNumber=int(input("Enter 1 for Student's Average Mark, 2 for Module's Average Mark, 3 to print students report or 4 to print modules report:  "))




#2.5
if(programNumber==3):
    print("Printing Students' Report")
    
    #print("Student Name", " ", "Average for the registered modules")
    #for i in range(STUDENTS):    
    #    print(students[i], "           ", averageMarksByStudentNumber(i, tableName=marks))

    
    #create the list of student averages
    studentAverageList=[]
    for i in range(STUDENTS):
        studentAverageList.append(averageMarksByStudentNumber(i, tableName=marks))
    print(studentAverageList)

    #sort the list
    for j in sortList(studentAverageList):
        print(studentAverageList[j], end=" ")
    
    print()

    #create the sorted list
    sortedList=[]
    for j in sortList(studentAverageList):
        sortedList.append(studentAverageList[j])
    print(sortedList)

    #join the students list with the averages list
    finalSortedAverages, finalSortedStudents = zip(*sorted(zip(studentAverageList, students), key=operator.itemgetter(0), reverse=True))

    print(finalSortedAverages)
    print(finalSortedStudents)
    
    #print the report with the sorted list
    print("Student Name", " ", "Average for the registered modules")
    for i in range(STUDENTS):
        #for i in range(STUDENTS):
        print(finalSortedStudents[i], "           ", finalSortedAverages[i])
    
#2.6
elif(programNumber==4):
    print("Printing Modules' Report")
    #for i in range(MODULES):
        #print(averageMarksByModuleNumber(i, tableName=marks))

    #print("Module Name", " ", "Average for the registered students")
    #for i in range(MODULES):
    #    print(modules[i], "         ", averageMarksByModuleNumber(i, tableName=marks))

    #create the list of module averages
    moduleAverageList=[]
    for i in range(MODULES):
        moduleAverageList.append(averageMarksByModuleNumber(i, tableName=marks))
    print(moduleAverageList)

    #join the students list with the averages list
    finalSortedAverages, finalSortedModules = zip(*sorted(zip(moduleAverageList, modules), key=operator.itemgetter(0), reverse=True))
    print(finalSortedAverages)
    print(finalSortedModules)

    print("Module Name", " ", "Average for the registered students")
    for i in range(MODULES):
        print(finalSortedModules[i], "         ", finalSortedAverages[i])

else:
    print("Invalid entry.  Bye")
