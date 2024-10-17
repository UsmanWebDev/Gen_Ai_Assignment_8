
from .department import Department

class Library(Department):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.list_of_books: list[str] = []
        self.list_of_categories: list[str] = []

    def add_book(self, book_name: str) -> None:
        self.list_of_books.append(book_name)

    def add_category(self, category_name: str) -> None:
        self.list_of_categories.append(category_name)

    def show_library(self) -> None:
        print(f"\n{'-'*10} Library Info {'-'*10}")
        print(f"Books: {', '.join(self.list_of_books)}")
        print(f"Categories: {', '.join(self.list_of_categories)}")
        print(f"{'-'*35}\n")
