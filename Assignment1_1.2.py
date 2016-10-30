print("Coursework 1 - 1.2 - List containing the given set of elements in the given order")
print("_________________________________________________________________________________")

listA=[]
listB=[]
listC=[]
searchedValue1 = 1
searchedValue2 = 2
searchedValue3 = 3
numOfElements = int(input("How many elements would you like in your list?  "))

for i in range(numOfElements):
    num=int(input("Please enter numbers to be added to your list: "))
    listA.append(num)
print("Your list is",listA)
    
if 1 in listA and 2 in listA and 3 in listA:
    print("")
    print("1, 2 and 3 appear in your list.  Let's see if they occur in the right order")
    print("")
    pos1 = listA.index(searchedValue1)

    listB = listA[pos1 : ]
    print("The contents of your list after the first 1 are:", listB)
    print("")

    if 2 in listB:
        pos2 = listB.index(searchedValue2)

        listC = listB[pos2 : ]
        print("The contents of your list from the 2 which followed your first 1 are:", listC)
        print("")

        if 3 in listC:
            print("YES")
            print("1, 2 and 3 appear in the list and they occur in the right order")
        else:
            print("NO")
            print("Even though 1, 2 and 3 appear in your list, they are not in the right order.  3 does not appear after the 2")
        
    else:
        print("NO")
        print("Even though 1, 2 and 3 appear in your list, they are not in the right order.  2 does not appear after the 1")
    
else:
    print("NO")
    print("Your list doesn't contain all of the numbers 1, 2 and 3")
