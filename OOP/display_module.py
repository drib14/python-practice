def display_records(records):
    print("\n----- DISPLAY RECORDS -----\n")

    if not records:
        print("No records available. \n")
        return

    for index, (student_id, data) in enumerate(records.items(), start=1):
        print(f"{index}. ID Number: {student_id}")
        print(f"   First Name: {data['first_name']}")
        print(f"   Last Name: {data['last_name']}")
        print(f"   Age: {data['age']}")
        print(f"   Course: {data['course']}")

    print("\n----- END OF RECORDS -----")
    input("Press ENTER to continue...")
