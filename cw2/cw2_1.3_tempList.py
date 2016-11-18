A=[2,0,1,1,3,1,1,1,4,1]
B=[1,1,1]
listOfIndexes=[2, 3, 5, 6, 7, 9]
m=len(B)

for i in range(len(listOfIndexes)):
    tempList1=list(A)
    tempList2=tempList1[listOfIndexes[i]:len(A)]
    print(listOfIndexes)
    print("tempList:",tempList1)
    print("evaluating:",tempList1[i:i+m])
    if tempList1[i:i+m]==B:
        print("Yes")
    else:
        print("No")
    #m=m+1
    
