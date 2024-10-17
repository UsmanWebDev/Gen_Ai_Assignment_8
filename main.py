
from university_management import University, Human, Assets, Campus, Department, Library, Classes, Student, Teacher


if __name__ == "__main__":

    
    # Create University
    university = University("National Technology of Space")
    university.show_info()

    
    # Human Resources
    human_resources = Human("National Technology of Space")
    human_resources.add_labor("Ahmed")
    human_resources.add_teacher("Fatima")
    human_resources.add_student("Hassan")
    human_resources.add_librarian("Ayesha")
    human_resources.show_human_resources()


   
    # Assets Management
    university_assets = Assets("National Technology of Space")
    university_assets.add_bus("Bus 1")
    university_assets.add_computer("Dell PC")
    university_assets.add_AC("Samsung AC")
    university_assets.show_assets()


 
    # Campus Management
    university_campus = Campus("National Technology of Space")
    university_campus.add_campus("Electronic")
    university_campus.add_campus("Computer")
    university_campus.add_campus("Civil")
    university_campus.show_campuses()

  
    # Department Info
    cs_department = Department("Computer Science Department")
    cs_department.add_library("CS Library")
    cs_department.add_class("CS101")
    cs_department.add_class("CS102")
    cs_department.show_department_info()


    # Library Management
    cs_library = Library("CS Library")
    cs_library.add_book("Data Structures in Python")
    cs_library.add_category("Programming")
    cs_library.show_library()

    # Classes Info
    available_classes = Classes()
    available_classes.show_classes()

  
    # Student Info
    student1 = Student("Ali", "112233", "CS101", "Fatima", student_CR=True)
    student1.show_student_info()

    # Teacher Info
    teacher1 = Teacher("Dr. Ibrahim", "T-101", "CS101", ["Class A", "Class B"], teacher_head_of_department=False)
    teacher1.show_teacher_info()