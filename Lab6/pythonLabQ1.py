"""Q1: Student marks management using nested dictionaries."""

SUBJECTS = ("Maths", "Physics", "Chemistry")
records: dict[str, dict] = {}


def read_int(prompt: str, minimum: int | None = None, maximum: int | None = None) -> int:
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Enter a value of at least {minimum}.")
                continue
            if maximum is not None and value > maximum:
                print(f"Enter a value no greater than {maximum}.")
                continue
            return value
        except ValueError:
            print("Please enter a whole number.")


def add_student() -> None:
    roll = input("Roll number: ").strip()
    if not roll or roll in records:
        print("Roll number is empty or already exists.")
        return
    name = input("Student name: ").strip()
    marks = {subject: read_int(f"{subject} marks (0-100): ", 0, 100) for subject in SUBJECTS}
    records[roll] = {"name": name, "marks": marks}
    print("Student added.")


def update_student() -> None:
    roll = input("Roll number to update: ").strip()
    student = records.get(roll)
    if student is None:
        print("Student not found.")
        return
    print("1. Update name  2. Update subject marks")
    choice = input("Choose: ").strip()
    if choice == "1":
        student["name"] = input("New name: ").strip()
    elif choice == "2":
        subject = input(f"Subject {SUBJECTS}: ").strip().title()
        if subject not in SUBJECTS:
            print("Unknown subject.")
            return
        student["marks"][subject] = read_int("New marks (0-100): ", 0, 100)
    else:
        print("Invalid choice.")
        return
    print("Record updated.")


def show_records() -> None:
    if not records:
        print("No student records available.")
        return
    for roll, student in records.items():
        print(f"{roll} | {student['name']} | {student['marks']}")


def show_reports() -> None:
    if not records:
        print("No records to analyse.")
        return
    averages = {roll: sum(data["marks"].values()) / len(SUBJECTS) for roll, data in records.items()}
    topper = max(averages, key=averages.get)
    print("Student averages:")
    for roll, average in averages.items():
        print(f"{records[roll]['name']} ({roll}): {average:.2f}")
    print(f"Class topper: {records[topper]['name']} ({averages[topper]:.2f})")
    for subject in SUBJECTS:
        best_roll = max(records, key=lambda roll: records[roll]["marks"][subject])
        print(f"Top in {subject}: {records[best_roll]['name']} — {records[best_roll]['marks'][subject]}")
    low = [(roll, data["name"], subject, mark)
           for roll, data in records.items()
           for subject, mark in data["marks"].items() if mark < 40]
    print("Marks below 40:", low if low else "None")


def main() -> None:
    while True:
        print("\nSTUDENT RECORDS\n1 Add  2 Update  3 Delete  4 View  5 Reports  0 Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            roll = input("Roll number to delete: ").strip()
            print("Deleted." if records.pop(roll, None) is not None else "Student not found.")
        elif choice == "4":
            show_records()
        elif choice == "5":
            show_reports()
        elif choice == "0":
            break
        else:
            print("Choose a valid menu option.")


if __name__ == "__main__":
    main()
