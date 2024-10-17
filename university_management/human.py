
from .university import University

class Human(University):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.list_of_labor: list[str] = []
        self.list_of_teacher: list[str] = []
        self.list_of_student: list[str] = []
        self.list_of_librarian: list[str] = []

    def add_labor(self, labor: str) -> None:
        self.list_of_labor.append(labor)

    def add_teacher(self, teacher: str) -> None:
        self.list_of_teacher.append(teacher)

    def add_student(self, student: str) -> None:
        self.list_of_student.append(student)

    def add_librarian(self, librarian: str) -> None:
        self.list_of_librarian.append(librarian)

    def show_human_resources(self) -> None:
        print(f"\n{'-'*10} Human Resources {'-'*10}")
        print(f"Labor: {', '.join(self.list_of_labor)}")
        print(f"Teachers: {', '.join(self.list_of_teacher)}")
        print(f"Students: {', '.join(self.list_of_student)}")
        print(f"Librarians: {', '.join(self.list_of_librarian)}")
        print(f"{'-'*35}\n")
