def update_record(records):
    print("\n----- UPDATE RECORD MENU -----")

    if not records:
        print("No records available.\n")
        return

    try:
        user_id = int(input("Enter ID to update: ").strip())
    except:
        print("Invalid ID.")
        return

    if user_id not in records:
        print("Record not found.\n")
        return

    record = records[user_id]

    while True:
        print("\nCurrent Record:")
        print(f"1. First Name: {record['first_name']}")
        print(f"2. Last Name : {record['last_name']}")
        print(f"3. Age       : {record['age']}")
        print(f"4. Course    : {record['course']}")
        print("5. Finish\n")

        choice = input("Choose field to update: ").strip()

        if choice == "1":
            record["first_name"] = input("New First Name: ").strip()

        elif choice == "2":
            record["last_name"] = input("New Last Name: ").strip()

        elif choice == "3":
            try:
                record["age"] = int(input("New Age: ").strip())
            except:
                print("Invalid age.")

        elif choice == "4":
            record["course"] = input("New Course: ").strip()

        elif choice == "5":
            print("Update complete!\n")
            break

        else:
            print("Invalid choice.")
