print("Coursework 1 - 2.1 - Counting left and right brackets")
print("_____________________________________________________")

left=0
right=0

S = input("enter a string of left and right brackets: ")
print(S)

for i in range(len(S)):
    if S[i] == '(':
        left = left + 1
    elif S[i] == ')':
        right = right + 1
print("you entered", left, "left and", right, "right brackets" )
