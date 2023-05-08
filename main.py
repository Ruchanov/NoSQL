import service

while True:
    print("Select an option:")
    print("1. Create table")
    print("2. Delete table")
    print("3. Read table")
    print("4. Add row")
    print("5. Delete row")
    print("6. Update row")
    print("7. Exit")
    choice = input()

    if choice == "1":
        name = input("Enter table name: ")
        columns = input("Enter columns (comma-separated): ").split(",")
        service.create_table(name, columns)
        print("Table created successfully.")

    elif choice == "2":
        name = input("Enter table name: ")
        service.delete_table(name)
        print("Table deleted successfully.")

    elif choice == "3":
        name = input("Enter table name: ")
        columns = input("Enter columns (comma-separated, leave blank for all): ")
        columns = [c.strip() for c in columns.split(",")] if columns else None
        rows = service.read_table(name, columns=columns)
        print("Table contents:")
        for row in rows:
            print(row)
        
    elif choice == "4":
        name = input("Enter table name: ")
        row = {}
        for col in columns:
            value = input(f"Enter value for {col}: ")
            row[col] = value
        service.add_row(name, row)
        print("Row added successfully.")

    elif choice == "5":
        name = input("Enter table name: ")
        id = input("Enter row ID: ")
        service.delete_row(name, id)
        print("Row deleted successfully.")

    elif choice == "6":
        name = input("Enter table name: ")
        id = input("Enter row ID: ")
        new_data = {}
        for col in columns:
            value = input(f"Enter new value for {col}: ")
            new_data[col] = value
        service.update_row(name, id, new_data)
        print("Row updated successfully.")

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
