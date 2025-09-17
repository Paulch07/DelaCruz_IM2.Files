items = []

size = int(input("Enter Matrix size: "))
for i in range(size):
    item = input(f"Shopping items {i+1}: ")
    items.append(item)

print(f"\nYou have {len(items)} items in the cart")

while True:
    option = input("\n[A]dd,[C]hange,[R]emove,[D]isplay,[S]earch  (* to exit): ").upper()

    if option == "*":
        print("Program ended.")
        break

    elif option == "A":
        item = input("Enter new item: ")
        items.append(item)
        print("Item added.")

    elif option == "C":
        key = int(input("Enter key: "))
        if 0 <= key < len(items):
            items[key] = input("New value: ")
        else:
            print("Key not found.")

    elif option == "R":
        key = int(input("Enter key: "))
        if 0 <= key < len(items):
            items.pop(key)
            print("Item has been removed.")
        else:
            print("Key not found.")

    elif option == "D":
        print("\nKey   Value")
        for k, v in enumerate(items):
            print(f"{k:<5} {v}")

    elif option == "S":
        key = int(input("Enter key: "))
        if 0 <= key < len(items):
            print("Result:", items[key])
        else:
            print("Key not found.")

    else:
        print("Invalid choice.")
