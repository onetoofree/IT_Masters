#prefix/suffix testing
LongStr=input("Please enter a long string ")
ShortStr=input("Please enter a short string ")
longlen=len(LongStr)
shortlen=len(ShortStr)
if(shortlen>longlen):
  print("String ",ShortStr," is neither a prefix nor a suffix of string ",LongStr)
else:
  ispref=1
  for i in range (0,shortlen):
     if(ShortStr[i]!=LongStr[i]):
          ispref=0
          break
  if (ispref==1):
     print("String ",ShortStr," is a prefix of a string ",LongStr)
  else:
     print("String ",ShortStr," is not a prefix of a string ",LongStr)

  issuff=1
  for i in range (0,shortlen):
      if(ShortStr[shortlen-1-i]!=LongStr[longlen-1-i]):
          issuff=0
          break
  if (issuff==1):
     print("String ",ShortStr," is a suffix of a string ",LongStr)
  else:
     print("String ",ShortStr," is not a suffix of a string ",LongStr)
