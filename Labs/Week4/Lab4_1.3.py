listA = []
yesList=[]
noList=[]

num = int(input("gimme numbers to put in list:  "))
while (num != 0):
    listA.append(num)
    num = int(input("gimme another number:  "))
print (listA)

for i in range(0, len(listA)-1):
    if listA[i] > listA[i+1]:
        noList.append("no")
    else:
        yesList.append("yes")

if len(noList) == 0:
    print("sorted")
else:
    print("not sorted")
    
