listA=[]
listB=[]
countListA=0
countListB=0
listAFinalState=[]

num=int(input("give me a number to add to the list: "))
while (num !=0):
    listA.append(num)
    num = int(input("give me another number to add to the list: "))
print("The contents of your list are:", listA)

for i in range(len(listA)):
    if listA[-1] == 1:
        print("the last character is a 1")
