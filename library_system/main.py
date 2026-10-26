
from book import Book
from member import Member
from library import Library


def main():
    library = Library()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Display Books")
        print("4. Display Members")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            book_id = input("Enter book ID: ").strip()
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()

            if book_id and title and author:
                library.add_book(Book(book_id, title, author))
            else:
                print("All fields are required.")

        elif choice == "2":
            member_id = input("Enter member ID: ").strip()
            name = input("Enter member name: ").strip()
            email = input("Enter member email: ").strip()

            if member_id and name and email:
                library.add_member(
                    Member(member_id, name, email)
                )
            else:
                print("All fields are required.")

        elif choice == "3":
            library.display_books()

        elif choice == "4":
            library.display_members()

        elif choice == "5":
            member_id = input("Enter member ID: ").strip()
            book_id = input("Enter book ID: ").strip()
            library.borrow_book(member_id, book_id)

        elif choice == "6":
            member_id = input("Enter member ID: ").strip()
            book_id = input("Enter book ID: ").strip()
            library.return_book(member_id, book_id)

        elif choice == "7":
            print("Thank you for using the Library System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
          
