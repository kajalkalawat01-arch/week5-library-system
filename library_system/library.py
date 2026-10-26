
import json
from pathlib import Path


class Library:
    def __init__(self, data_file="library_data.json"):
        self.books = {}
        self.members = {}
        self.data_file = Path(data_file)
        self.load_data()

    def add_book(self, book):
        if book.book_id in self.books:
            print("Book ID already exists.")
            return

        self.books[book.book_id] = book
        self.save_data()
        print("Book added successfully!")

    def add_member(self, member):
        if member.member_id in self.members:
            print("Member ID already exists.")
            return

        self.members[member.member_id] = member
        self.save_data()
        print("Member added successfully!")

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
            return

        if not book:
            print("Book not found.")
            return

        if member.borrow_book(book):
            self.save_data()

    def return_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)

        if not member:
            print("Member not found.")
            return

        if not book:
            print("Book not found.")
            return

        if member.return_book(book):
            self.save_data()

    def save_data(self):
        data = {
            "books": [
                {
                    "book_id": book.book_id,
                    "title": book.title,
                    "author": book.author,
                    "is_borrowed": book.is_borrowed,
                    "due_date": (
                        str(book.due_date)
                        if book.due_date else None
                    )
                }
                for book in self.books.values()
            ],
            "members": [
                {
                    "member_id": member.member_id,
                    "name": member.name,
                    "email": member.email,
                    "borrowed_books": member.borrowed_books
                }
                for member in self.members.values()
            ]
        }

        self.data_file.parent.mkdir(
            parents=True, exist_ok=True
        )
        with open(self.data_file, "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        if not self.data_file.exists():
            return

        try:
            with open(self.data_file, "r") as file:
                data = json.load(file)

            from book import Book
            from member import Member
            from datetime import date

            for item in data.get("books", []):
                book = Book(
                    item["book_id"],
                    item["title"],
                    item["author"]
                )
                book.is_borrowed = item.get(
                    "is_borrowed", False
                )
                due_date = item.get("due_date")
                book.due_date = (
                    date.fromisoformat(due_date)
                    if due_date else None
                )
                self.books[book.book_id] = book

            for item in data.get("members", []):
                member = Member(
                    item["member_id"],
                    item["name"],
                    item["email"]
                )
                member.borrowed_books = item.get(
                    "borrowed_books", []
                )
                self.members[member.member_id] = member

        except (json.JSONDecodeError, KeyError, ValueError):
            print("Could not load library data.")
      
