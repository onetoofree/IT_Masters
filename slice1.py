listA=[1,2,3,2,1,2,3,4,3,2,1,2,3,4,5,4,3,2,1,2,3,4,1,3,1,4,2]
listB=[]
finalListToCheck=[]
count=0
print(listA)

##for i in listA:
for i in range(len(listA)):
##    print (i, listA[i])
    if listA[i] == 1:
        listB.append(i)
print(listB)
numberOfElementsInListA = len(listA)
numberOfElementsInListB = len(listB)
print(numberOfElementsInListA)
print(numberOfElementsInListB)
positionOfLast1inListB = (numberOfElementsInListB - 1)
print(positionOfLast1inListB)
print(listA[listB[positionOfLast1inListB]])
positionOfLast1=(listB[-1])
print(positionOfLast1)

remainder = (len(listA)) - (listB[-1])
print(remainder)

if (remainder < 3):
    print("let's do some stuff - Slice!")
    finalListToCheck=listA[ : positionOfLast1]
##    finalListToCheck[ : 16]
    print(finalListToCheck)
else:
    print("nothing to slice here - do check on all")
    print(listA)
