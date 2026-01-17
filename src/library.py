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
    def generate_report(self):
        report = ["ID | Title | Author | Status"]
        for book_id, info in self.books.items():
            report.append(
                f"{book_id} | {info['title']} | {info['author']} | {info['status']}"
            )
        return "\n".join(report)
