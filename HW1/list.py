Row = int(input("Row: "))
Col = int(input("Col: "))
nested_list = []
for x in range(Row):
    print(f"Row{x+1}")
    innerlist = []
    for y in range(Col):
        print(f"Col{y+1}")
        score = float(input())
        innerlist.append(score)
    nested_list.append(innerlist)
for x in range(len(nested_list)):
    for y in range(len(nested_list[x])):
        print(nested_list[x][y], end=" ")
    print()
mylist = [[],[]]
for x in range(len(mylist)):
    for y in range(len(mylist[x])):
        print("Enter Score: ")
        num = float(input())
        mylist.append(num)
search = float(input())

position = []

for i in range(Row):
    for j in range(Col):
        if nested_list[i][j] == search:
            position.append((i+1,j+1))
print(f"\n Number {search} found at, {position}")