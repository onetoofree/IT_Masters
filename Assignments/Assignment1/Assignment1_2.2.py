print("Coursework 1 - 2.2 - Counting left and right brackets")
print("_____________________________________________________")

counter=0
counterList=[]

S = input("enter a string of left and right brackets: ")
print(S)

for i in range(len(S)):
    if S[i] == '(':
        counter = counter+1
        counterList.append(counter)
    elif S[i] == ')':
        counter = counter-1
        counterList.append(counter)

if int(-1) in counterList or S[-1]=='(' or len(S) % 2 !=0:
    print("NO")
    print("Your string is not math-like")
else:
    print("YES")
    print("Your string is math-like")
