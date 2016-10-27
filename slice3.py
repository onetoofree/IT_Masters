listA=[0,2,3,4,1,2,3,1,2,3,1,2,4,1,1,1,1,1,2,1,1,]
listB=[]
yesList=[]
noList=[]
listToCheck=[]
count=0
print(listA)
readyToCheck = False
print(len(listA)-1)
print(listA[-2])

while listA[-1]==1:
    for i in range(len(listA)):
        if listA[-1] == 1:
            listA=listA[ :(len(listA)-1)]
        #elif listA[-2] == 1:
         #   listA=listA[ :(len(listA)-1)]
print(listA)
