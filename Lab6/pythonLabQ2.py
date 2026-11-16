"""Q2: Employee payroll and department analytics."""

employees: dict[str, dict] = {}


def read_salary(prompt: str) -> float:
    while True:
        try:
            salary = float(input(prompt))
            if salary <= 0:
                print("Salary must be positive.")
                continue
            return salary
        except ValueError:
            print("Enter a valid amount.")


def add_employee() -> None:
    emp_id = input("Employee ID: ").strip()
    if not emp_id or emp_id in employees:
        print("ID is empty or already exists.")
        return
    employees[emp_id] = {
        "name": input("Name: ").strip(),
        "department": input("Department: ").strip().title(),
        "salary": read_salary("Monthly salary: "),
    }
    print("Employee added.")


def show_reports() -> None:
    if not employees:
        print("No employee data available.")
        return
    total_payroll = sum(person["salary"] for person in employees.values())
    print(f"Total monthly payroll: ₹{total_payroll:,.2f}")
    departments = {person["department"] for person in employees.values()}
    for department in sorted(departments):
        team = {emp_id: person for emp_id, person in employees.items() if person["department"] == department}
        average = sum(person["salary"] for person in team.values()) / len(team)
        highest_id = max(team, key=lambda emp_id: team[emp_id]["salary"])
        print(f"{department}: {len(team)} employee(s), average ₹{average:,.2f}, top earner {team[highest_id]['name']}")
    print("Salary ranking:")
    for emp_id, person in sorted(employees.items(), key=lambda item: item[1]["salary"], reverse=True):
        print(f"{person['name']} ({emp_id}): ₹{person['salary']:,.2f}")
    revised = {emp_id: round(person["salary"] * 1.10, 2) for emp_id, person in employees.items()}
    print("10% raise preview:", revised)


def main() -> None:
    while True:
        print("\nEMPLOYEE PAYROLL\n1 Add  2 Update salary  3 Delete  4 Search  5 List  6 Reports  0 Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_employee()
        elif choice == "2":
            emp_id = input("Employee ID: ").strip()
            if emp_id in employees:
                employees[emp_id]["salary"] = read_salary("New salary: ")
                print("Salary updated.")
            else:
                print("Employee not found.")
        elif choice == "3":
            emp_id = input("Employee ID: ").strip()
            print("Deleted." if employees.pop(emp_id, None) is not None else "Employee not found.")
        elif choice == "4":
            term = input("Employee ID or department: ").strip().lower()
            matches = {key: value for key, value in employees.items()
                       if key.lower() == term or value["department"].lower() == term}
            print(matches if matches else "No matching employee.")
        elif choice == "5":
            for emp_id, person in employees.items():
                print(emp_id, person)
        elif choice == "6":
            show_reports()
        elif choice == "0":
            break
        else:
            print("Choose a valid menu option.")


if __name__ == "__main__":
    main()
