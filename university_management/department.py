
from .campus import Campus

class Department(Campus):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.list_of_library: list[str] = []
        self.list_of_classes: list[str] = []

    def add_library(self, library: str) -> None:
        self.list_of_library.append(library)

    def add_class(self, class_name: str) -> None:
        self.list_of_classes.append(class_name)

    def show_department_info(self) -> None:
        print(f"\n{'-'*10} Department Info {'-'*10}")
        print(f"Libraries: {', '.join(self.list_of_library)}")
        print(f"Classes: {', '.join(self.list_of_classes)}")
        print(f"{'-'*35}\n")
