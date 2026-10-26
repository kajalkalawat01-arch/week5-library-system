
from datetime import date, timedelta


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.due_date = None

    def borrow(self, days=14):
        if self.is_borrowed:
            print("This book is already borrowed.")
            return False

        self.is_borrowed = True
        self.due_date = date.today() + timedelta(days=days)
        print(f"'{self.title}' borrowed successfully.")
        print(f"Due date: {self.due_date}")
        return True

    def return_book(self):
        if not self.is_borrowed:
            print("This book has not been borrowed.")
            return False

        today = date.today()

        if today > self.due_date:
            overdue_days = (today - self.due_date).days
            print(f"Book is overdue by {overdue_days} day(s).")
        else:
            print("Book returned on time.")

        self.is_borrowed = False
        self.due_date = None
        print(f"'{self.title}' returned successfully.")
        return True

    def display_info(self):
        status = "Borrowed" if self.is_borrowed else "Available"

        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")

        if self.due_date:
            print(f"Due Date: {self.due_date}")
          
