A=[]
B=[]
C=[]
D=[]
copyOfA=[]
listOfIndexes=[]
tempList=[]
yesList=[]
noList=[]

numOfElementsA = int(input("How many elements would you like in your list A?  "))
numOfElementsB = int(input("How many elements would you like in your list B?  "))
print("")

for i in range(numOfElementsA):
    num=int(input("Please enter numbers to be added to your list A: "))
    A.append(num)
print("Your list is",A)

for i in range(numOfElementsB):
    num=int(input("Please enter numbers to be added to your list B: "))
    B.append(num)
print("Your list is",B)

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
    #print("gonna check some more stuff out")
    for i in range(len(B)):
        if B[i] in A:
            for i,e in enumerate(A):
                D.append(i)
                D=D[ :len(A)]
#print ("List D is a list of list A's indexes : ",D)
copyOfA=list(A)
#print(A)
#print(copyOfA)
if len(A)>len(B):
    for i in range(len(copyOfA)):
        if B[0] in copyOfA:          
            listOfIndexes.append(copyOfA.index(B[0]))
            copyOfA.insert(copyOfA.index(B[0]), 'x')
            copyOfA.pop(copyOfA.index(B[0]))
#print(listOfIndexes)
#print(A)
#print(copyOfA)

for i in range(len(listOfIndexes)):
    m=len(B)
    tempList1=list(A)
    tempList2=tempList1[listOfIndexes[i]:listOfIndexes[i]+m]
 #   print("tempList1:",tempList1)
 #   print("indexList:",listOfIndexes)
 #   print("tempList2:",tempList1[listOfIndexes[i]:listOfIndexes[i]+m])
 #   print(listOfIndexes[i])
 #   print(listOfIndexes[i]+m)
 #   print("m:",m)
 #   print("length of B",len(B))
    if tempList2==B:
        #print("Yes")
        #print("")
        yesList.append("yes")
    else:
        #print("No")
        #print("")
        noList.append("no")

if "yes" in yesList:
    print("YES")
    print("The elements of B appear in A in the same order as in B consecutively")
else:
    print("NO")
    print("The elements of B do not appear in A in the same order as in B consecutively")

