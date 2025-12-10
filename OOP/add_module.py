def add_record(records):
    print("\n----- ADD RECORD MENU -----")

    while True:
        user_id_input = input("Enter ID number: ").strip()

        try:
            user_id = int(user_id_input)
        except:
            print("Invalid ID. Must be numeric.")
            continue

        if user_id in records:
            print("This ID is already used.\n")
            return

        first = input("Enter First Name: ").strip()
        last = input("Enter Last Name: ").strip()

        try:
            age = int(input("Enter Age: ").strip())
        except:
            print("Invalid Age.")
            continue

        course = input("Enter Course: ").strip()

        # Save
        records[user_id] = {
            "first_name": first,
            "last_name": last,
            "age": age,
            "course": course
        }

        print("Record successfully added!")
        input("Press ENTER to continue...\n")
        return
