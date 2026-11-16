"""Q3: Library inventory and book lending with nested dictionaries."""

books: dict[str, dict] = {}


def add_book() -> None:
    isbn = input("ISBN: ").strip()
    if not isbn:
        print("ISBN cannot be empty.")
        return
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    try:
        copies = int(input("Number of copies to add: "))
        if copies <= 0:
            raise ValueError
    except ValueError:
        print("Copies must be a positive whole number.")
        return
    if isbn in books:
        books[isbn]["total_copies"] += copies
        books[isbn]["available"] += copies
    else:
        books[isbn] = {"title": title, "author": author, "total_copies": copies,
                       "available": copies, "borrowers": [], "ever_issued": False}
    print("Book stock updated.")


def issue_book() -> None:
    isbn = input("ISBN to issue: ").strip()
    if isbn not in books:
        print("Book not found.")
        return
    member = input("Member name: ").strip()
    borrowed_count = sum(member in book["borrowers"] for book in books.values())
    if borrowed_count >= 2:
        print("A member may borrow at most two different books at a time.")
    elif books[isbn]["available"] <= 0:
        print("No copy is currently available.")
    elif member in books[isbn]["borrowers"]:
        print("This member has already borrowed this title.")
    else:
        books[isbn]["available"] -= 1
        books[isbn]["borrowers"].append(member)
        books[isbn]["ever_issued"] = True
        print("Book issued.")


def return_book() -> None:
    isbn = input("ISBN to return: ").strip()
    member = input("Member name: ").strip()
    if isbn not in books or member not in books[isbn]["borrowers"]:
        print("No matching active loan found.")
        return
    books[isbn]["borrowers"].remove(member)
    books[isbn]["available"] += 1
    print("Book returned.")


def show_reports() -> None:
    if not books:
        print("No books in the catalogue.")
        return
    by_author: dict[str, list[str]] = {}
    borrowers: dict[str, list[str]] = {}
    for isbn, book in books.items():
        by_author.setdefault(book["author"], []).append(book["title"])
        for member in book["borrowers"]:
            borrowers.setdefault(member, []).append(book["title"])
    print("Titles by author:", by_author)
    print("Members with multiple books:", {name: titles for name, titles in borrowers.items() if len(titles) > 1})
    print("Out-of-stock titles:", [book["title"] for book in books.values() if book["available"] == 0])
    print("Never-issued titles:", [book["title"] for book in books.values() if not book["ever_issued"]])


def main() -> None:
    while True:
        print("\nLIBRARY\n1 Add book  2 Issue  3 Return  4 Search  5 View catalogue  6 Reports  0 Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_book()
        elif choice == "2":
            issue_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            term = input("ISBN or title keyword: ").strip().lower()
            matches = {isbn: book for isbn, book in books.items()
                       if term in isbn.lower() or term in book["title"].lower()}
            print(matches if matches else "No matching book.")
        elif choice == "5":
            print(books if books else "Catalogue is empty.")
        elif choice == "6":
            show_reports()
        elif choice == "0":
            break
        else:
            print("Choose a valid menu option.")


if __name__ == "__main__":
    main()
