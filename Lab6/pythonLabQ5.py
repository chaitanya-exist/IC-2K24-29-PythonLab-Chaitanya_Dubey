"""Q5: Contact directory with unique phone numbers and reverse lookup."""

contacts: dict[str, dict] = {}
phone_index: dict[str, str] = {}


def valid_phone(phone: str) -> bool:
    return len(phone) == 10 and phone.isdigit()


def add_contact() -> None:
    name = input("Contact name: ").strip()
    if not name or name in contacts:
        print("Name is empty or already exists.")
        return
    phone = input("10-digit phone number: ").strip()
    if not valid_phone(phone) or phone in phone_index:
        print("Phone number is invalid or already assigned.")
        return
    email = input("Email: ").strip()
    city = input("City: ").strip().title()
    contacts[name] = {"phones": [phone], "email": email, "city": city}
    phone_index[phone] = name
    print("Contact added.")


def add_number() -> None:
    name = input("Contact name: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    phone = input("Additional 10-digit number: ").strip()
    if not valid_phone(phone) or phone in phone_index:
        print("Phone number is invalid or already assigned.")
        return
    contacts[name]["phones"].append(phone)
    phone_index[phone] = name
    print("Number added.")


def update_contact() -> None:
    name = input("Contact name: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    contacts[name]["email"] = input("New email: ").strip()
    contacts[name]["city"] = input("New city: ").strip().title()
    print("Contact updated.")


def delete_contact() -> None:
    name = input("Contact name: ").strip()
    contact = contacts.pop(name, None)
    if contact is None:
        print("Contact not found.")
        return
    for phone in contact["phones"]:
        phone_index.pop(phone, None)
    print("Contact deleted.")


def show_reports() -> None:
    by_city: dict[str, list[str]] = {}
    for name, contact in contacts.items():
        by_city.setdefault(contact["city"], []).append(name)
    print("Contacts grouped by city:", {city: sorted(names) for city, names in sorted(by_city.items())})
    print("Phone-to-name reverse index:", phone_index)


def main() -> None:
    while True:
        print("\nCONTACT DIRECTORY\n1 Add  2 Add another number  3 Update  4 Delete  5 Search name  6 Reverse phone lookup  7 List  8 Reports  0 Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            add_number()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            term = input("Name or part of name: ").strip().lower()
            matches = {name: data for name, data in contacts.items() if term in name.lower()}
            print(matches if matches else "No matching contact.")
        elif choice == "6":
            phone = input("Phone number: ").strip()
            print("Contact:", phone_index.get(phone, "No matching contact."))
        elif choice == "7":
            print(contacts if contacts else "Directory is empty.")
        elif choice == "8":
            show_reports()
        elif choice == "0":
            break
        else:
            print("Choose a valid menu option.")


if __name__ == "__main__":
    main()
