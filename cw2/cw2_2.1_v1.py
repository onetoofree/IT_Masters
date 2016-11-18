STUDENTS = 5
MODULES = 4

marks =[
    [42, 76, 62, 55]
    [94, 87, 76, 95]
    [72, 24, 95, 86]
    [86, 55, 67, 92]
    [100, 46, 51, 62]
]

results=marks[3][1]

for i in range(STUDENTS):
    for j in range(MODULES):
        print("%8d" % marks[i][j], end="")
print()
