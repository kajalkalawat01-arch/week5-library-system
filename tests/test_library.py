
import unittest
import tempfile
import os
import sys

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "library_system")
    )
)

from book import Book
from member import Member
from library import Library


class TestLibrarySystem(unittest.TestCase):

    def test_book_creation(self):
        book = Book("B1", "Python Basics", "John Smith")
        self.assertEqual(book.title, "Python Basics")
        self.assertFalse(book.is_borrowed)

    def test_borrow_and_return_book(self):
        book = Book("B2", "Learn Python", "Jane Smith")
        self.assertTrue(book.borrow())
        self.assertTrue(book.is_borrowed)
        self.assertTrue(book.return_book())
        self.assertFalse(book.is_borrowed)

    def test_add_book_and_member(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_file = os.path.join(temp_dir, "library_data.json")
            library = Library(data_file)

            book = Book("B3", "OOP Basics", "Alex")
            member = Member("M1", "Kajal", "kajal@example.com")

            library.add_book(book)
            library.add_member(member)

            self.assertIn("B3", library.books)
            self.assertIn("M1", library.members)

    def test_save_and_load_data(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_file = os.path.join(temp_dir, "library_data.json")

            library = Library(data_file)
            library.add_book(Book("B4", "Python Guide", "Sam"))
            library.add_member(
                Member("M2", "Riya", "riya@example.com")
            )

            loaded_library = Library(data_file)

            self.assertIn("B4", loaded_library.books)
            self.assertIn("M2", loaded_library.members)


if __name__ == "__main__":
    unittest.main()
  
