#Modules and marks
Modules=["Calculus1","Calculus2","Calculus3","Programming1","Programming2","Programming3"]
Marks=[50,80,35,70,62,15]
mode=int(input("Please enter 0 for printout with classification, 1 without classification "))
if(mode==0):
     for i in range (0,len(Modules)):
          print(Modules[i]," ",Marks[i])
else:
     print("Modules with first class marks")
     #note that the lists are explored four times, each time with the appropriate filtering condition
     for i in range (0,len(Modules)):
       if(Marks[i]>=70):
          print(Modules[i]," ",Marks[i])

     print("Modules with 2:1 marks")
     for i in range (0,len(Modules)):
       if(Marks[i]>=60 and Marks[i]<=69):
          print(Modules[i]," ",Marks[i])

     print("Modules with 2:2 marks")
     for i in range (0,len(Modules)):
       if(Marks[i]>=50 and Marks[i]<=59):
          print(Modules[i]," ",Marks[i])

     print("Failed modules")
     for i in range (0,len(Modules)):
       if(Marks[i]<50):
          print(Modules[i]," ",Marks[i])
