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
