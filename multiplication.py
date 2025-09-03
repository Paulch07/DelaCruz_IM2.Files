while True:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    if rows <= 0 or cols <= 0:
        print("Invalid Input!")
        break

    # Generate multiplication table
    table = []
    for i in range(1, rows + 1):
        row = []
        for j in range(1, cols + 1):
            row.append(i * j)
            print(f"{i * j:4}", end=" ")
        table.append(row)
        print()

    # Search and highlight
    search = int(input("Enter value to search: "))
    isFound = False

    
    for row in table:
        for value in row:
            if value == search:
                print(f"[{value:2}]", end=" ")
                isFound = True
            else:
                print(f"{value:4}", end=" ")
        print()
        
        
    if isFound:
        print("\nValue found! ")
    else:
        print("\n Value not found!' ")
    break