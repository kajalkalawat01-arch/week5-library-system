
import unittest
import os
import sys

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "library_system")
    )
)

from member import Member


class TestMember(unittest.TestCase):

    def test_member_creation(self):
        member = Member("M1", "Kajal", "kajal@example.com")
        self.assertEqual(member.member_id, "M1")
        self.assertEqual(member.name, "Kajal")
        self.assertEqual(member.email, "kajal@example.com")

    def test_borrowed_books_initially_empty(self):
        member = Member("M2", "Riya", "riya@example.com")
        self.assertEqual(len(member.borrowed_books), 0)


if __name__ == "__main__":
    unittest.main()
  
