def display_records(records):
    print("\n----- DISPLAY RECORDS -----\n")

    if not records:
        print("No records available.\n")
        return

    for index, (student_id, data) in enumerate(records.items(), start=1):
        print(f"{index}.  First Name: {data['first_name']}")
        print(f"    Last Name : {data['last_name']}")
        print(f"    ID Number : {student_id}")
        print(f"    Age       : {data['age']}")
        print(f"    Course    : {data['course']}\n")

    print("----- END OF RECORDS -----")
    input("Press ENTER to continue...\n")
