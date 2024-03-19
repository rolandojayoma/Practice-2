phone_book = {}

while True:
    print("\nPhone Book:")
    print("1. Add contact")
    print("2. Look up contact")
    print("3. Delete contact")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")
        phone_book[name] = number
        print("Contact added successfully.")
    elif choice == '2':
        name = input("Enter contact name: ")
        print(phone_book.get(name, f"{name} is not found in the phone book."))
    elif choice == '3':
        name = input("Enter contact name: ")
        if name in phone_book:
            del phone_book[name]
            print("Contact deleted successfully.")
        else:
            print(f"{name} is not found in the phone book.")
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")
