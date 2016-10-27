A=[]
counter=0
howManyElements = int(input("How many elements would you like in your list?  "))
print(howManyElements)

for i in range(howManyElements):
    entry = int(input("enter a number: "))
    A.append(entry)
print(A)

for i in range(len(A)):
    if A[i] == 4:
        counter = counter + 1
print("you entered", counter, "fours")
