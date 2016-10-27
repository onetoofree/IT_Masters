#sum of even and odd numbers, for version
SumEven=0
SumOdd=0

listlen=int(input("How many numbers would you like to enter? "))
for i in range (1,listlen+1):
     num=int(input("Please enter a number "))
     if(num%2==0):
       SumEven=SumEven+num
     else:
       SumOdd=SumOdd+num
print("The sum of even numbers is ",SumEven)
print("The sum of odd numbers is ",SumOdd)
