A=[2,0,1,1,3,1,1,1,4,1]
B=[1,1,1]
listOfIndexes=[2, 3, 5, 6, 7, 9]
m=len(B)
yesList=[]
noList=[]

for i in range(len(listOfIndexes)):
    tempList1=list(A)
    tempList2=tempList1[listOfIndexes[i]:listOfIndexes[i]+m]
    print("tempList1:",tempList1)
    print("indexList:",listOfIndexes)
    print("tempList2:",tempList1[listOfIndexes[i]:listOfIndexes[i]+m])
    if tempList2==B:
        print("Yes")
        print("")
        yesList.append("yes")
    else:
        print("No")
        print("")
        noList.append("no")
    #m=m+1
if "yes" in yesList:
    print("YES")
    print("The elements of B appear in A in the same order as in B consecutively")
else:
    print("NO")
    print("The elements of B do not appear in A in the same order as in B consecutively")
