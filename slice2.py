listA=[0,2,3,4,1,2,3,1,2,3,1,2,4,1]
listB=[]
yesList=[]
noList=[]
listToCheck=[]
count=0
print(listA)
readyToCheck = False
print(len(listA)-1)

for i in range(len(listA)):
    if listA[-1] == 1:
        listToCheck=listA[ :(len(listA)-1)]
print(listToCheck)
        
        

    

'''
for i in range(len(listA)):
    if listA[i] == 1:
        listB.append(i)
print(listB)

for i in range(len(listA)):
    if listA[i] == 1:
        if listA[i] == 1 and listA[i+1] == 2 and listA[i+2] == 3:
            yesList.append("yes")
        else:
            noList.append("no")
#print(listOfYes)
#print(listOfNo)
 
if "yes" in yesList:
    print("Yes - the sequence 1,2,3 appears")
else:
    print("No - 123 does not appear")
'''
