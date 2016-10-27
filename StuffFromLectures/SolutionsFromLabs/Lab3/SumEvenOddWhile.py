#sum of even and odd numbers, while version
SumEven=0
SumOdd=0

num=int(input("Please enter a number "))
while (num !=0):
 if(num%2==0):
   SumEven=SumEven+num
 else:
   SumOdd=SumOdd+num
 num=int(input("Please enter a number "))

print("The sum of even numbers is ",SumEven)
print("The sum of odd numbers is ",SumOdd)
     
