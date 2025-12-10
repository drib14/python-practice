def delete_record(records):
    print("\n----- DELETE RECORD MENU -----")

    if not records:
        print("No records available.\n")
        return

    try:
        user_id = int(input("Enter ID to delete: ").strip())
    except:
        print("Invalid ID.")
        return

    if user_id not in records:
        print("Record not found.\n")
        return

    data = records[user_id]

    print("\nRecord to delete:")
    print(f"First Name: {data['first_name']}")
    print(f"Last Name : {data['last_name']}")
    print(f"Age       : {data['age']}")
    print(f"Course    : {data['course']}\n")

    confirm = input("Are you sure? (Y/N): ").lower()

    if confirm == "y":
        del records[user_id]
        print("Record deleted!\n")
    else:
        print("Deletion cancelled.\n")

    input("Press ENTER to continue...")
