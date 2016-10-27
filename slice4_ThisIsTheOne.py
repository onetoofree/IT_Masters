listA=[0,2,3,4,1,2,3,1,2,3,1,1,4,3,1,1,1,1,1,1,1,1,2,1]

print(listA)

print(len(listA)-1)
print(listA[-2])

for i in range(len(listA)):
    while listA[-1] == 1 or listA[-2]==1:
        if listA[-1] == 1: 
            listA=listA[ :(len(listA)-1)]
        elif listA[-2] == 1:
            listA=listA[ :(len(listA)-1)]
print(listA)
