import unittest
from src.library import Library

class TestSprint1(unittest.TestCase):

    def setUp(self):
        self.lib = Library()

    def test_add_book_success(self):
        self.lib.add_book(1, "Python", "Guido")
        self.assertIn(1, self.lib.books)

    def test_duplicate_book_id(self):
        self.lib.add_book(1, "Python", "Guido")
        with self.assertRaises(ValueError):
            self.lib.add_book(1, "Java", "James")

if __name__ == "__main__":
    unittest.main()
