MEDALS = 3
COUNTRIES = 7
countries = ["Canada",
             "China",
             "Germany",
             "Korea",
             "Japan",
             "Russia",
             "United States"]


counts =[
    [1 ,0, 1],
    [1 ,1, 0],
    [1 ,0, 0],
    [1 ,1, 1],
    [0 ,0, 1],
    [0 ,0, 1],
    [1 ,0, 1]
]

print("        Country          Gold      Silver      Bronze      Total")

for i in range(COUNTRIES):
    print("%15s" % countries[i], end="")

    total=0
    for j in range(MEDALS):
        print("%12d" % counts[i][j], end="")
        total = total + counts[i][j]

    print("%12d" % total)
