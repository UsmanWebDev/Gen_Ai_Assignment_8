
from .classes import Classes

class Teacher(Classes):
    def __init__(self, teacher_name: str, teacher_number: str, teacher_subject: str, teacher_of_classes: list[str], teacher_head_of_department: bool = False) -> None:
        super().__init__()
        self.teacher_name: str = teacher_name
        self.teacher_number: str = teacher_number
        self.teacher_subject: str = teacher_subject
        self.teacher_of_classes: list[str] = teacher_of_classes
        self.teacher_head_of_department: bool = teacher_head_of_department

    def show_teacher_info(self) -> None:
        hod_status: str = "Yes" if self.teacher_head_of_department else "No"
        print(f"\n{'-'*10} Teacher Info {'-'*10}")
        print(f"Teacher Name: {self.teacher_name}")
        print(f"Teacher Number: {self.teacher_number}")
        print(f"Subject: {self.teacher_subject}")
        print(f"Classes: {', '.join(self.teacher_of_classes)}")
        print(f"Head of Department: {hod_status}")
        print(f"{'-'*35}\n")
