# Input rows and columns
Row = int(input("Row: "))
Col = int(input("Col: "))

# Build dictionary {(row, col): value}
matrix_dict = {}
for x in range(Row):
    print(f"Row {x+1}")
    for y in range(Col):
        score = float(input(f"  Col {y+1}: "))
        matrix_dict[(x+1, y+1)] = score

# Display matrix
print("\nThe numbers are:")
for i in range(1, Row+1):
    for j in range(1, Col+1):
        print(matrix_dict[(i, j)], end=" ")
    print()

# Search for a value
search = float(input("\nSearch: "))

# Find positions with that value
positions = [pos for pos, val in matrix_dict.items() if val == search]

# Output result
if positions:
    print(f"\nNumber {search} found at: {positions}")
else:
    print(f"\nNumber {search} not found.")
