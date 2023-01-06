class Book:

    def __init__(self, author: str, title: str):
        self.author = author
        self.title = title

    def __repr__(self) -> str:
        return f"{self.author}: {self.title}"


class Library:

    def __init__(self, *books: Book):
        self.books = list(books)

    def append_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        self.books.remove(book)

    def find_books(self, **options: any) -> [Book]:
        books = []
        for book in self.books:
            for option, value in options.items():
                if getattr(book, option) != value:
                    break
            else:
                books.append(book)
        return books

    def sort_books(self, option: str, reverse: bool = False):
        self.books.sort(key=lambda book: getattr(book, option), reverse=reverse)

home_library = Library(
    Book("Марк Лутц", "5-е издание Изучаем Python Том 1")
)

print(home_library.books)

home_library.append_book(
    Book("Саша Грей", "Общество Жюльетты")
)

print(home_library.books)
see = "Саша Грей"
print(home_library.find_books(author=see))