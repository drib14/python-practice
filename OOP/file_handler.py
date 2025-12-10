import os

FILE_PATH = r"Z:\PT332\practice\OOP\data.txt"


def load_records():
    """Load records from data.txt (ID first format)."""
    records = {}

    if not os.path.exists(FILE_PATH):
        return records

    with open(FILE_PATH, "r") as file:
        lines = [line.rstrip() for line in file]

    current_id = None
    temp = {}

    for line in lines:
        # Skip start/end markers
        if "=== START OF RECORDS ===" in line or "=== END OF RECORDS ===" in line:
            continue

        # Detect start of a record → "1. ID Number: 1"
        if ". ID Number:" in line:
            if current_id is not None:
                records[current_id] = temp

            temp = {}
            current_id = int(line.split(":")[1].strip())
            continue

        if "First Name:" in line:
            temp["first_name"] = line.split(":")[1].strip()
        elif "Last Name:" in line:
            temp["last_name"] = line.split(":")[1].strip()
        elif "Age:" in line:
            temp["age"] = int(line.split(":")[1].strip())
        elif "Course:" in line:
            temp["course"] = line.split(":")[1].strip()

    # Save last record
    if current_id is not None:
        records[current_id] = temp

    return records


def save_records(records):
    """Save all records with ID first format."""
    with open(FILE_PATH, "w") as file:
        file.write("=== START OF RECORDS ===\n")
        for index, (student_id, data) in enumerate(records.items(), start=1):
            file.write(f"\n{index}. ID Number: {student_id}\n")
            file.write(f"   First Name: {data['first_name']}\n")
            file.write(f"   Last Name: {data['last_name']}\n")
            file.write(f"   Age: {data['age']}\n")
            file.write(f"   Course: {data['course']}\n")
        file.write("\n=== END OF RECORDS ===\n")
