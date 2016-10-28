A=[]
lengthOfList = int(input("Enter the numbner of elements: "))
for i in range (lengthOfList):
    elm = int(input("Enter an element value: "))
    A.append(elm)

#print(A)
minVal = A[0]
minValIndex=0
for i in range(1, lengthOfList):
    if minVal>A[i]:
        minVal = A[i]
        minValIndex = i
print (minVal, "at index", minValIndex)

