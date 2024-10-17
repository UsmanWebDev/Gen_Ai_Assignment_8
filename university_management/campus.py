
from .university import University

class Campus(University):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.list_of_campus: list[str] = []

    def add_campus(self, campus_name: str) -> None:
        self.list_of_campus.append(campus_name)

    def show_campuses(self) -> None:
        print(f"\n{'-'*10} University Campuses {'-'*10}")
        print(f"Campuses: {', '.join(self.list_of_campus)}")
        print(f"{'-'*35}\n")
