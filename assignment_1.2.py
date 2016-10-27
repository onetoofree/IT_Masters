listA=[]
listB=[]
listC=[]
searchedValue1 = 1
searchedValue2 = 2
searchedValue3 = 3

num=int(input("give me a number to add to the list: "))
while (num !=0):
    listA.append(num)
    num = int(input("give me another number to add to the list: "))
print("The contents of your list are:", listA)
    
if 1 in listA and 2 in listA and 3 in listA:
    print("")
    print("yes - 1, 2 and 3 appear in your list.  Let's see if they occur in the right order")
    print("")
    pos1 = listA.index(searchedValue1)

    listB = listA[pos1 : ]
    print("The contents of your list after the first 1 are:", listB)
    print("")

    if 2 in listB:
        pos2 = listB.index(searchedValue2)

        listC = listB[pos2 : ]
        print("The contents of your list after the 2 which followed your first 1 are:", listC)
        print("")

        if 3 in listC:
            print("Yes!  1, 2 and 3 appear in the list and they occur in the right order")
        else:
            print("No - even though 1, 2 and 3 appear in your list, they are not in the right order.  There is no 3 after the 2")
        
    else:
        print("No - even though 1, 2 and 3 appear in your list, they are not in the right order.  There is no occurance of 2 after the 1")
    
else:
    print("No - 1, 2 and 3 don't all appear")
