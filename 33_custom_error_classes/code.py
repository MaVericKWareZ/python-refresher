class TooManyPagesReadException(ValueError):
    def __init__(self, book: "Book", pages: int):
        self.msg = f"You tried to read {pages}, but {book.name} has {book.page_count} pages"

    def __str__(self):
        return self.msg


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name}, {self.page_count} pages, {self.pages_read} read>"
        )

    def read(self, pages: int):
        if pages+self.pages_read > self.page_count:
            raise TooManyPagesReadException(book, pages)
        else:
            self.pages_read += pages
            print(f"You have read {self.pages_read} now!")


book = Book("ABC", 300)
try:
    book.read(500)
except TooManyPagesReadException as e:
    print(e)
else:
    print(f"Read successful!!")
finally:
    print(book)
