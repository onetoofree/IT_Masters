'''
A=[]
lengthOfList = int(input("Enter the numbner of elements: "))
for i in range (lengthOfList):
    elm = int(input("Enter an element value: "))
    A.append(elm)
'''

A=[8,4,3,3,6,9,3,9,3,1]
#print(A)
minVal = A[0]
minValIndex=0
#for i in range(lengthOfList):
for i in range(1, len(A)):
    if minVal>=A[i]:
        minVal = A[i]
        #minValIndex = i
#print (minVal, "at index", minValIndex)
listOfIndex = []
for i in range(0, len(A)):
    if (minVal==A[i]):
        listOfIndex.append(i)
print (minVal, "appears at index", listOfIndex)
