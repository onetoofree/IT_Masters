print("Coursework 1 - 1.3 - List containing the given set of elements consecutively and in the given order")
print("___________________________________________________________________________________________________")

A=[]

yesList = []
noList = []
listLengthError=""
 
numOfElements = int(input("How many elements would you like in your list?  "))
for i in range(numOfElements):
    num=int(input("Please enter numbers to be added to your list: "))
    A.append(num)
print("Your list is",A)
print("")
 
for i in range(len(A)):
    try:
        while A[-1] == 1 or A[-2]==1:
            if A[-1] == 1:
                A=A[ :(len(A)-1)]
            elif A[-2] == 1:
                A=A[ :(len(A)-1)]
    except Exception as e:
        listLengthError="The sequence 1,2,3 does not appear."
      
#print("If either of the last two characters in your list are 1, the program will crash.")
#print("So, your list has been inspected to see if either of the last two characters are 1.")
#print("If 1 was found in either position, the offending 1s were sliced from your list as many times as necessary to prevent the crash without affecting the program's functionality.")
#print("If not, your full list has remained intact.")
#print("The list that will be inspected for the sequence 1,2,3 is:")
#print(A)
#print("")

for i in range(len(A)):
    if A[i] == 1:
        if A[i] == 1 and A[i+1] == 2 and A[i+2] == 3:
            yesList.append("yes")
        else:
            noList.append("no")
if len(listLengthError) > 0:
    print("NO")
    print(listLengthError)
elif "yes" in yesList:
    print("YES")    
    print("The sequence 1,2,3 appears")
else:
    print("NO")
    print("The sequence 1,2,3 does not appear")
