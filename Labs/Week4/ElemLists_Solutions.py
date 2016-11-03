#Elementary operations with lists
n=int(input("Please enter the list length "))
A=[]
for i in range (0,n):
    print("Entering element ",i)
    CurEl=int(input("Please enter the element "))
    A.append(CurEl)
 
 
#Computing the index of the smallest element
minind=0 #initialization of the smallest element index
for i in range (1,n):
  if(A[i]<A[minind]):
            minind=i
print("The index of the smallest element is ",minind)
 
A.remove(A[minind]) #removal of a smallest element
 
#repeating the same min search routine
#the smallest element found this time will be the second smallest
#in the original list
mindind=0 #initialization of the smallest element index
for i in range (1,n-1): #note the list became 1 shorter!
  if(A[i]<A[minind]):
            minind=i
print("The second smallest element is ",A[minind])
 
#checking sortedness of the list
sorted=1
for i in range (1,n):
     if(A[i-1]>A[i]):
          sorted=0
          break
if(sorted==1):
     print("Sorted")
else:
     print("Not Sorted")
