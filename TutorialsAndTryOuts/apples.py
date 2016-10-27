apples =0
oranges =0
while oranges != -1:
    print("Enter number of apples: ")
    apples=float(input())
    print("Enter number of oranges: ")
    oranges=float(input())
    if oranges == 0:
        continue
    print (apples + oranges)
