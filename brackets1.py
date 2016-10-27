S=[]
left=0
right=0
counter=0
howManyBrackets = int(input("How many elements would you like in your list?  "))
print(howManyBrackets)

for i in range(howManyBrackets):
    entry = input("enter a symbol: ")
    S.append(entry)
print(S)

for i in range(len(S)):
    if S[i] == '(':
        left = left + 1
    elif S[i] == ')':
        right = right + 1
print("you entered", left, "left and", right, "right brackets" )

for i in range(howManyBrackets):
    #if S[0] == '(' and S[-1] == ')':
    if S[0] == ')' or S[-1] == '(':
        print("you started with ) or ended with (")
        print("bad maths - no go.")
        break
        #print("you started with ( and ended with )")
    if S[1] == ')' and S[2] == ')':
        print("Dude - you started with ()) - that can't run")
        print("off too a bad start - not maths")
        break
    if S[i] == '(':
        counter = counter + 1
        #print(counter)
    else:
        counter = counter - 1
        #print(counter)
    if counter == 0:
        print("yes maths")
    else:
        print("not maths")

'''
If starts with a ( and ends with a )
do something
set a variable to something
True for example
if var is set to True, do the further check - the plus minus check
if not true, return not maths
also,
do a count at the start
if it's an odd number, it can't be maths
needs to be even
check that first
and then check that it starts with ( and ends with )
'''        
    
