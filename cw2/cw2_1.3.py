A=[2,4,6,8,10,2,4,6,8,10,2,4,6,8,10,2,4,6,8,10]
B=[2,4,6,8,10,2,4,6,8,10]
#A=[4,2,6,8,2,3,5,6,8,9,9,5,3,2,4,2,6,7]
#B=[2,3,5,6,8,9,9]
C=[]
D=[]
copyOfA=[]
listOfIndexes=[]
tempList=[]
m=len(B)
yesList=[]
noList=[]

#numOfElementsA = int(input("How many elements would you like in your list A?  "))
#numOfElementsB = int(input("How many elements would you like in your list B?  "))
#print("")

#for i in range(numOfElementsA):
#    num=int(input("Please enter numbers to be added to your list A: "))
#    A.append(num)
#print("Your list is",A)

#for i in range(numOfElementsB):
#    num=int(input("Please enter numbers to be added to your list B: "))
#    B.append(num)
#print("Your list is",B)

if len(A)==len(B):
    if A==B:
        print("YES")
        print("The elements of B appear in A in the same order as in B consecutively.  They are exactly the same")
        raise SystemExit
    else:
        print("NO")
        print("Elements of B do not appear in A in the same order consecutively")
        raise SystemExit

if len(A)<len(B):
    print("NO")
    print("Elements of B do not appear in A in the same order consecutively.")
    raise SystemExit

if len(A)>len(B):
    print("gonna check some stuff out")
    #this check does a basic check on the index of B[i] in A.  Not good enough as it only gets the first ocurrance
    for i in range(len(B)):
        if B[i] in A:
            C.append(A.index(B[i]))
print (C)

#I want to get all occurances.
#One approach is to enumerate A to get the index of all
#Once I have the index of all, I would be interested only in the index of those whose value is the same as the first element in B.
#From that I can create a list starting from that index, the length of B

#If that doesn't work, I can try this
#Get the index as done above
#Add the index to a list
#For the element whose index I just got, change the value to x
#And repeat - get index, add to list and change to x
#Do this until all necessary elements are changed to x

if len(A)>len(B):
    print("gonna check some more stuff out")
    for i in range(len(B)):
        if B[i] in A:
            for i,e in enumerate(A):
                D.append(i)
                D=D[ :len(A)]
print ("list D: ",D)
copyOfA=list(A)
print(A)
print(copyOfA)
if len(A)>len(B):
    for i in range(len(copyOfA)):
        if B[0] in copyOfA:
            
            listOfIndexes.append(copyOfA.index(B[0]))
            copyOfA.insert(copyOfA.index(B[0]), 'x')
            copyOfA.pop(copyOfA.index(B[0]))
print(listOfIndexes)
print(A)
print(copyOfA)

#for i in range(len(listOfIndexes)):
#    tempList=list(A)
#    print("tempList:",tempList)
#    tempList=tempList[:len(B)]
#print("tempList:",tempList)

for i in range(len(listOfIndexes)):
    tempList1=list(A)
    tempList2=tempList1[listOfIndexes[i]:listOfIndexes[i]+m]
    print("tempList1:",tempList1)
    print("indexList:",listOfIndexes)
    print("tempList2:",tempList1[listOfIndexes[i]:listOfIndexes[i]+m])
    print(listOfIndexes[i])
    print(listOfIndexes[i]+m)
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

