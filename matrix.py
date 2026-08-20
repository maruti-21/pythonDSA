rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = list(map(int, input(f"Enter elements of row {i+1}: ").split()))
    matrix.append(row)

print("Biggest number from each row:")

for row in matrix:
    print(max(row))