#counting the number of occurrences of the given symbol in the given string
MyStr=input("Please enter a string ")
symb=input("Please enter=symbol ")
count=0
for i in range(0,len(MyStr)):
     if(MyStr[i]==symb):
          count=count+1
print("The number of symbols ",symb," in ",MyStr," is ",count)
