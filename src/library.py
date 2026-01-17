class Library:
    def __init__(self):
        self.books = {}
    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise ValueError("Duplicate book ID")

        self.books[book_id] = {
            "title": title,
            "author": author,
            "status": "Available"
        }
    def borrow_book(self, book_id):
        if self.books[book_id]["status"] == "Borrowed":
            raise ValueError("Book already borrowed")

        self.books[book_id]["status"] = "Borrowed"
    def return_book(self, book_id):
        self.books[book_id]["status"] = "Available"
