from add_module import add_record
from update_module import update_record
from delete_module import delete_record
from display_module import display_records
from file_handler import load_records, save_records


def main_menu():
    records = load_records()

    while True:
        print("MAIN MENU:")
        print("1. Add Record")
        print("2. Display Records")
        print("3. Delete Record")
        print("4. Update Record")
        print("5. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            add_record(records)
            save_records(records)

        elif choice == "2":
            display_records(records)

        elif choice == "3":
            delete_record(records)
            save_records(records)

        elif choice == "4":
            update_record(records)
            save_records(records)

        elif choice == "5":
            save_records(records)
            print("\nExiting...\n")
            break

        else:
            print("Invalid input. Choose 1–5.\n")


if __name__ == "__main__":
    main_menu()
