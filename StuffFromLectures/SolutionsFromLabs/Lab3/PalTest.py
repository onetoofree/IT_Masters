#palindrome testing
MyStr=input("Please enter a string ")
ispal=1
mylen=len(MyStr)
for i in range (0,mylen):
     if(MyStr[i]!=MyStr[mylen-1-i]):
        ispal=0
        break
if(ispal==1):
  print("String ",MyStr," is a palindrome")
else:
  print("String ",MyStr," is not a palindrome")
