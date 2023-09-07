rows = int(input("Rows:"))
colums = int(input("Colums:"))

for i in range(1,rows + 1):
    print(i, end=" ")
    numb = i
    for j in range(1, colums):
        numb += rows
        print(numb, end=" ")
    print(" ")



