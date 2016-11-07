print("Coursework 1 - 1.2 - List containing the given set of elements in the given order")
print("_________________________________________________________________________________")

A=[]
B=[]
C=[]
searchedValue1 = 1
searchedValue2 = 2
searchedValue3 = 3
numOfElements = int(input("How many elements would you like in your list?  "))

for i in range(numOfElements):
    num=int(input("Please enter numbers to be added to your list: "))
    A.append(num)
print("Your list is",A)
    
if 1 in A and 2 in A and 3 in A:
    print("")
    print("1, 2 and 3 appear in your list.  Let's see if they occur in the right order")
    print("")
    pos1 = A.index(searchedValue1)

    B = A[pos1 : ]
    print("The contents of your list after the first 1 are:", B)
    print("")

    if 2 in B:
        pos2 = B.index(searchedValue2)

        C = B[pos2 : ]
        print("The contents of your list from the 2 which followed your first 1 are:", C)
        print("")

        if 3 in C:
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
