listA = []
listB = []
num = int(input("gimme numbers to put in list:  "))
while (num != 0):
    listA.append(num)
    num = int(input("gimme another number:  "))
print (listA)

lowestNum=listA[0]
while len(listB) < 2:
    for i in range(1, len(listA)):
        if listA[i] < lowestNum:
            lowestNum = listA[i]
            listB.append(lowestNum)
            listA.remove(lowestNum)
print (listB[1])
    



'''
print("The lowest number in the list is:", lowestNum)
print("The position of the lowest number is:" ,listA.index(lowestNum))
print("I'm deleting it.  BYE!")
listA.remove(lowestNum)
print(listA)

lowestNum=listA[0]
print("So, now - the lowest number in the list is....(AKA the second lowest)")

    for i in range(0, len(listA)):
        if listA[i] < lowestNum:
            lowestNum = listA[i]

print("The lowest number in the list is:", lowestNum)
'''
