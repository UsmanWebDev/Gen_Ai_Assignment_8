
from .classes import Classes

class Student(Classes):
    def __init__(self, student_name: str, student_roll_no: str, student_subject: str, student_teacher: str, student_CR: bool = False) -> None:
        super().__init__()
        self.student_name: str = student_name
        self.student_roll_no: str = student_roll_no
        self.student_subject: str = student_subject
        self.student_teacher: str = student_teacher
        self.student_CR: bool = student_CR

    def show_student_info(self) -> None:
        cr_status: str = "Yes" if self.student_CR else "No"
        print(f"\n{'-'*10} Student Info {'-'*10}")
        print(f"Student Name: {self.student_name}")
        print(f"Roll No: {self.student_roll_no}")
        print(f"Subject: {self.student_subject}")
        print(f"Teacher: {self.student_teacher}")
        print(f"Class Representative: {cr_status}")
        print(f"{'-'*35}\n")
