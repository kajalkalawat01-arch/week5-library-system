
import unittest
import os
import sys

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "library_system")
    )
)

from book import Book


class TestBook(unittest.TestCase):

    def test_book_creation(self):
        book = Book("B1", "Python Basics", "John Smith")
        self.assertEqual(book.title, "Python Basics")
        self.assertEqual(book.author, "John Smith")
        self.assertFalse(book.is_borrowed)

    def test_borrow_book(self):
        book = Book("B2", "Learn Python", "Jane Smith")
        result = book.borrow()
        self.assertTrue(result)
        self.assertTrue(book.is_borrowed)

    def test_return_book(self):
        book = Book("B3", "Python Guide", "Alex")
        book.borrow()
        result = book.return_book()
        self.assertTrue(result)
        self.assertFalse(book.is_borrowed)


if __name__ == "__main__":
    unittest.main()
      
