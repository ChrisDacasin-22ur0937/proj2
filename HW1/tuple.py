Row = int(input("Row: "))
Col = int(input("Col: "))


nested_tuple = ()
for x in range(Row):
    print(f"Row{x+1}")
    inner_tuple = ()
    for y in range(Col):
        print(f"Col{y+1}")
        score = float(input())
        inner_tuple += (score,)       
    nested_tuple += (inner_tuple,)   

for x in range(len(nested_tuple)):
    for y in range(len(nested_tuple[x])):
        print(nested_tuple[x][y], end=" ")
    print()

search = float(input("\nSearch: "))

position = ()
for i in range(Row):
    for j in range(Col):
        if nested_tuple[i][j] == search:
            position += ((i+1, j+1),)

print(f"\nNumber {search} found at: {position}")
