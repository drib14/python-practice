def add_record(records):
    print("\n----- Add Record -----")
    while True:
        user_id_input = input("Enter ID number: ").strip()
        if not user_id_input:
            print("\nID cannot be empty. Please enter a numeric ID.\n")
            continue
        try:
            user_id = int(user_id_input)
        except ValueError:
            print("\nInvalid ID. Please enter a numeric ID.\n")
            continue

        if user_id in records:
            print("\nID already being used.\n")
            return

        first_name = input("Enter First Name: ").strip()
        if not first_name:
            print("\nFirst Name cannot be empty.\n")
            continue

        last_name = input("Enter Last Name: ").strip()
        if not last_name:
            print("\nLast Name cannot be empty.\n")
            continue

        duplicate_name_found = False
        for info in records.values():
            if (info['first_name'].lower() == first_name.lower() and
                info['last_name'].lower() == last_name.lower()):
                duplicate_name_found = True
                break

        if duplicate_name_found:
            print("\nThis name already exists in the system.\n")
            return

        records[user_id] = {'first_name': first_name, 'last_name': last_name}
        print("\nRecord added successfully!\n")
        return


def display_records(records):
    print("\n----- All Records -----")
    if not records:
        print("No records available.\n")
    else:
        for user_id, info in records.items():
            print(f"ID: {user_id} | Name: {info['first_name']} {info['last_name']}")
        print()


def delete_record(records):
    print("\n----- Delete Record -----")
    if not records:
        print("No records available to delete.\n")
        return

    user_id_input = input("Enter ID number to delete: ").strip()
    if not user_id_input:
        print("\nID cannot be empty.\n")
        return
    try:
        user_id = int(user_id_input)
    except ValueError:
        print("\nInvalid ID. Please enter a numeric ID.\n")
        return

    if user_id in records:
        del records[user_id]
        print(f"\nRecord {user_id} deleted successfully!\n")
    else:
        print(f"\nID No. {user_id} not found.\n")


def update_record(records):
    print("\n----- Update Record -----")
    if not records:
        print("No records available to update.\n")
        return

    user_id_input = input("Enter ID number to update: ").strip()
    if not user_id_input:
        print("\nID cannot be empty.\n")
        return
    try:
        user_id = int(user_id_input)
    except ValueError:
        print("\nInvalid ID. Please enter a numeric ID.\n")
        return

    if user_id not in records:
        print(f"\nID No. {user_id} not found.\n")
        return

    print(f"\nCurrent Name: {records[user_id]['first_name']} {records[user_id]['last_name']}")
    first_name = input("Enter new First Name (leave blank to keep unchanged): ").strip()
    last_name = input("Enter new Last Name (leave blank to keep unchanged): ").strip()

    if not first_name and not last_name:
        print("\nNo changes made.\n")
        return

    if first_name:
        records[user_id]['first_name'] = first_name
    if last_name:
        records[user_id]['last_name'] = last_name

    print("\nRecord updated successfully!\n")


def main_menu():
    records = {}

    while True:
        print("Menu:")
        print("1. Add Record")
        print("2. Display All Records")
        print("3. Delete Record")
        print("4. Update Record")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice not in ['1', '2', '3', '4', '5']:
            print("\nInvalid input. Choose between 1 - 5 only!\n")
            continue

        if choice == '1':
            add_record(records)
        elif choice == '2':
            display_records(records)
        elif choice == '3':
            delete_record(records)
        elif choice == '4':
            update_record(records)
        else:
            print("\nExiting program. Goodbye!\n")
            break


if __name__ == "__main__":
    main_menu()
