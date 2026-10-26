
class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_borrowed:
            print("Sorry, this book is not available.")
            return False

        if book.borrow():
            self.borrowed_books.append(book.book_id)
            print(f"{self.name} borrowed '{book.title}'.")
            return True

        return False

    def return_book(self, book):
        if book.book_id not in self.borrowed_books:
            print("This member has not borrowed this book.")
            return False

        if book.return_book():
            self.borrowed_books.remove(book.book_id)
            print(f"{self.name} returned '{book.title}'.")
            return True

        return False

    def display_info(self):
        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Borrowed Books: {self.borrowed_books}")
      
