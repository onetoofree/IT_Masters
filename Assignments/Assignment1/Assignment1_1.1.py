print("Coursework 1 - 1.1 - List containing the given set of elements")
print("______________________________________________________________")

A=[]
numOfElements = int(input("How many elements would you like in your list?  "))

for i in range(numOfElements):
    num=int(input("Please enter numbers to be added to your list: "))
    A.append(num)
print("Your list is",A)
    
if 1 in A and 2 in A and 3 in A:
    print("YES")
    print("Your list contains the numbers 1, 2 and 3")
else:
    print("NO")
    print("Your list doesn't contain all of the numbers 1, 2 and 3")
