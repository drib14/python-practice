import os

FILE_PATH = r"Z:\PT332\practice\OOP\data.txt"


def load_records():
    """Load formatted records from data.txt"""
    records = {}

    if not os.path.exists(FILE_PATH):
        return records

    with open(FILE_PATH, "r") as file:
        lines = file.readlines()

    current_id = None
    temp = {}

    for line in lines:
        line = line.rstrip()

        # Detect start of record e.g. "1. First Name: John"
        if ".  First Name:" in line:
            # Save previous before resetting
            if current_id is not None:
                records[current_id] = temp

            temp = {}
            parts = line.split("First Name:")
            name = parts[1].strip()
            temp["first_name"] = name
            continue

        if "Last Name" in line:
            temp["last_name"] = line.split(":")[1].strip()

        elif "ID Number" in line:
            current_id = int(line.split(":")[1].strip())

        elif "Age" in line:
            temp["age"] = int(line.split(":")[1].strip())

        elif "Course" in line:
            temp["course"] = line.split(":")[1].strip()

    # save last record
    if current_id is not None:
        records[current_id] = temp

    return records


def save_records(records):
    """Save all records with START and END markers."""
    with open(FILE_PATH, "w") as file:
        file.write("=== START OF RECORDS ===\n\n")

        for index, (student_id, data) in enumerate(records.items(), start=1):
            file.write(f"{index}.  First Name: {data['first_name']}\n")
            file.write(f"    Last Name : {data['last_name']}\n")
            file.write(f"    ID Number : {student_id}\n")
            file.write(f"    Age       : {data['age']}\n")
            file.write(f"    Course    : {data['course']}\n\n")

        file.write("=== END OF RECORDS ===\n")
