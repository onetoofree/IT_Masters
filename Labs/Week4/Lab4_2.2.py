Marks=[50,80,35,70,62,15]
Modules=["Calculus1","Calculus2","Calculus3","Programming1","Programming2","Programming3"]

print("Modules with first class marks")
for i in range(len(Marks)):
    if (Marks[i] >=70):        
        print(Modules[i], Marks[i])
print()
        
print("Modules with 2:1 marks")
for i in range(len(Marks)):
    if (Marks[i] >=60 and Marks[i] < 70):        
        print(Modules[i], Marks[i])
print()

print("Modules with 2:2 marks")
for i in range(len(Marks)):
    if (Marks[i] >=50 and Marks[i] < 60):        
        print(Modules[i], Marks[i])
print()

print("Failed Modules")
for i in range(len(Marks)):
    if (Marks[i] <50):        
        print(Modules[i], Marks[i])

