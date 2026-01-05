mydict = {}

size = int(input("Enter number of shopping items: "))

for i in range(size):
    item = input(f"Shopping item {i+1}: ")
    mydict[i] = item

print("You have", len(mydict), "items in the cart.")

for key, value in mydict.items():
    print(f"Shopping item {key+1}: {value}")



while True:
    option = input(
        "\nWhat would you like to do "
        "[A]dd, [C]hange, [R]emove, [D]isplay, [S]earch (* to exit)? "
    ).upper()

    if option == "*":
        print("Bye!!")
        break

    elif option == "A":
        new_key = max(mydict.keys()) + 1
        new_item = input("Enter new item: ")
        mydict[new_key] = new_item
        print("Item added.")

    elif option == "C":
        search = input("Enter item number to change: ")
        if search.isdigit():
            key = int(search) - 1
            if key in mydict:
                print(f"Found {mydict[key]} item")
                new_value = input("Enter new value: ")
                mydict[key] = new_value
            else:
                print("I'm sorry, not in the cart")
        else:
            print("Invalid key")

    elif option == "R":
        search = input("Enter item number to remove: ")
        if search.isdigit():
            key = int(search) - 1
            if key in mydict:
                removed = mydict.pop(key)
                print(f"The item {search} with value '{removed}' has been deleted")
            else:
                print("Item not found")
        else:
            print("Invalid key")

    elif option == "D":
        print("\nItem No   Value")
        for key, value in mydict.items():
            print(f"{key+1:<8} {value}")

   
    elif option == "S":
        item = input("Enter item number or name to search: ")
        found = False

        if item.isdigit():
            key = int(item) - 1
            if key in mydict:
                print(f"Found '{mydict[key]}' as item {key+1}")
                found = True
        else:
            for key, value in mydict.items():
                if value.lower() == item.lower():
                    print(f"Found '{value}' as item {key+1}")
                    found = True
                    break

        if not found:
            print("Sorry not found!")

    else:
        print("Invalid option. Please choose again.")  
