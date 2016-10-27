listA=[]
countOf1s = 0
listOfYes = []
listOfNo = []

num=int(input("give me a number to add to the list: "))
while (num !=0):
    listA.append(num)
    num = int(input("give me another number to add to the list: "))
print("The contents of your list are:", listA)
    
if 1 in listA and 2 in listA and 3 in listA:
    print("")
    print("yes - 1, 2 and 3 appear in your list.  Let's see if they occur in the right order")
    print("")

    for i in range(len(listA)):
        if listA[i] == 1:
            if listA[i] == 1 and listA[i+1] == 2 and listA[i+2] == 3:
                listOfYes.append("yes")
            else:
                listOfNo.append("no")
#print(listOfYes)
#print(listOfNo)

if "yes" in listOfYes:
    print("Yes - the sequence 1,2,3 appears")
else:
    print("No - 123 does not appear")
        

    
    




'''
    for i in range(len(listA)):
        #if listA[i] == 1:
          #  countOf1s = countOf1s + 1
            #for i in range(countOf1s):
            if listA[i] == 1 and listA[i+1] == 2 and listA[i+2] == 3:
                print("yes")
            else:
                print("no")
    print(countOf1s)


'''


'''
    for i in range(len(listA)):
        if listA[i] == 1 and listA[i+1] == 2 and listA[i+2] == 3:
            print("yes my yoot!")
        else:
            print("nope")

'''
