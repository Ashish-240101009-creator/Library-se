import unittest
from src.library import Library

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.lib = Library()

    # -------- Sprint 1 Tests --------
    def test_add_book_success(self):
        self.lib.add_book(1, "Python", "Guido")
        self.assertIn(1, self.lib.books)

    def test_duplicate_book_id(self):
        self.lib.add_book(1, "Python", "Guido")
        with self.assertRaises(ValueError):
            self.lib.add_book(1, "Java", "James")

    # -------- Sprint 2 Tests --------
    def test_borrow_available_book(self):
        self.lib.add_book(1, "Python", "Guido")
        self.lib.borrow_book(1)
        self.assertEqual(self.lib.books[1]["status"], "Borrowed")

    def test_borrow_unavailable_book(self):
        self.lib.add_book(1, "Python", "Guido")
        self.lib.borrow_book(1)
        with self.assertRaises(ValueError):
            self.lib.borrow_book(1)

    def test_return_book(self):
        self.lib.add_book(1, "Python", "Guido")
        self.lib.borrow_book(1)
        self.lib.return_book(1)
        self.assertEqual(self.lib.books[1]["status"], "Available")
    # -------- Sprint 3 Tests --------
    def test_report_contains_header(self):
        report = self.lib.generate_report()
        self.assertIn("ID | Title | Author | Status", report)

    def test_report_contains_book_entry(self):
        self.lib.add_book(1, "Python", "Guido")
        report = self.lib.generate_report()
        self.assertIn("Python", report)

if __name__ == "__main__":
    unittest.main()
