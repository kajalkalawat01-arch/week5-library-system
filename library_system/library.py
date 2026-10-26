
           
import json
from pathlib import Path
from datetime import date

from book import Book
from member import Member


class Library:
    def __init__(self, data_file=None):
        self.books = {}
        self.members = {}

        if data_file is not None:
            self.data_file = Path(data_file)
            self.books_file = self.data_file
            self.members_file = self.data_file
            self.combined_file = True
        else:
            self.data_dir = Path(__file__).resolve().parent.parent / "data"
            self.books_file = self.data_dir / "books.json"
            self.members_file = self.data_dir / "members.json"
            self.combined_file = False

        self.load_data()

    def add_book(self, book):
        if book.book_id in self.books:
            print("Book ID already exists.")
            return False

        self.books[book.book_id] = book
        self.save_data()
        print("Book added successfully!")
        return True

    def add_member(self, member):
        if member.member_id in self.members:
            print("Member ID already exists.")
            return False

        self.members[member.member_id] = member
        self.save_data()
        print("Member added successfully!")
        return True

    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        for book in self.books.values():
            book.display_info()
            print("-" * 30)

    def display_members(self):
        if not self.members:
            print("No members registered.")
            return

        for member in self.members.values():
            member.display_info()
            print("-" * 30)

    def borrow_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)

        if not member:
            print("Member not found.")
            return False

        if not book:
            print("Book not found.")
            return False

        if member.borrow_book(book):
            self.save_data()
            return True

        return False

    def return_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)

        if not member:
            print("Member not found.")
            return False

        if not book:
            print("Book not found.")
            return False

        if member.return_book(book):
            self.save_data()
            return True

        return False

    def save_data(self):
        if self.combined_file:
            data = {
                "books": [self.book_to_dict(b) for b in self.books.values()],
                "members": [self.member_to_dict(m) for m in self.members.values()]
            }
            self.data_file.parent.mkdir(parents=True, exist_ok=True)
            with self.data_file.open("w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        else:
            self.data_dir.mkdir(parents=True, exist_ok=True)

            with self.books_file.open("w", encoding="utf-8") as file:
                json.dump(
                    [self.book_to_dict(b) for b in self.books.values()],
                    file,
                    indent=4
                )

            with self.members_file.open("w", encoding="utf-8") as file:
                json.dump(
                    [self.member_to_dict(m) for m in self.members.values()],
                    file,
                    indent=4
                )

    @staticmethod
    def book_to_dict(book):
        return {
            "book_id": book.book_id,
            "title": book.title,
            "author": book.author,
            "is_borrowed": book.is_borrowed,
            "due_date": str(book.due_date) if book.due_date else None
        }

    @staticmethod
    def member_to_dict(member):
        return {
            "member_id": member.member_id,
            "name": member.name,
            "email": member.email,
            "borrowed_books": member.borrowed_books
        }

    def load_data(self):
        try:
            if self.combined_file:
                if not self.data_file.exists():
                    return

                with self.data_file.open("r", encoding="utf-8") as file:
                    data = json.load(file)

                books_data = data.get("books", [])
                members_data = data.get("members", [])
            else:
                books_data = self.read_json(self.books_file)
                members_data = self.read_json(self.members_file)

            for item in books_data:
                book = Book(item["book_id"], item["title"], item["author"])
                book.is_borrowed = item.get("is_borrowed", False)
                due_date = item.get("due_date")
                book.due_date = date.fromisoformat(due_date) if due_date else None
                self.books[book.book_id] = book

            for item in members_data:
                member = Member(
                    item["member_id"],
                    item["name"],
                    item["email"]
                )
                member.borrowed_books = item.get("borrowed_books", [])
                self.members[member.member_id] = member

        except (json.JSONDecodeError, KeyError, ValueError, TypeError):
            print("Could not load library data.")

    @staticmethod
    def read_json(path):
        if not path.exists():
            return []

        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
            
      
