listA=[]
#listA=[0,2,3,4,1,2,2,3,1,2,2,3,1,1,4,3,1,1,1,1,1,1,1,1,2,3]
listOfYes = []
listOfNo = []

num=int(input("give me a number to add to the list: "))
while (num !=0):
    listA.append(num)
    num = int(input("give me another number to add to the list: "))
print("The contents of your list are:", listA)

print(listA)

for i in range(len(listA)):
    while listA[-1] == 1 or listA[-2]==1:
        if listA[-1] == 1: 
            listA=listA[ :(len(listA)-1)]
        elif listA[-2] == 1:
            listA=listA[ :(len(listA)-1)]
print(listA)
for i in range(len(listA)):
    if listA[i] == 1:
        if listA[i+1] exists? -listA[i+1] == 2:
            if listA[i+2] == 3:
                listOfYes.append("yes")
        else:
            listOfNo.append("no")

if "yes" in listOfYes:
    print("Yes - the sequence 1,2,3 appears")
else:
    print("No - 123 does not appear")
