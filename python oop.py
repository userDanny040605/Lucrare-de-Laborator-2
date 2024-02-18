# class Student:
#     def __init__(self, first_name, last_name, email, enrollment_date, dob):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.enrollment_date = enrollment_date
#         self.dob = dob
#
#     def get_firstname(self):
#         return self.first_name
#
#     def get_lastname(self):
#         return self.last_name
#
#     def get_email(self):
#         return self.email
#
#     def get_enrollment_date(self):
#         return self.enrollment_date
#
#     def get_dob(self):
#         return self.dob
#
#
# class Faculty:
#     def __init__(self):
#         self.students = []
#
#     def assign_student(self, student):
#         self.students.append(student)
#         print("Student has been assigned to Faculty")
#
#     def display_enrolled_students(self):
#         print("Students enrolled in faculty:")
#         for student in self.students:
#             print("First Name:", student.get_firstname())
#             print("Last Name: ", student.get_lastname())
#             print("Email: ", student.get_email())
#             print("Enrollment Date: ", student.get_enrollment_date())
#             print("Date of Birth: ", student.get_dob())
#
#             print("\n")
#
#
# def main():
#     faculty = Faculty()
#
#     while True:
#         print("\nFaculty")
#         print("1. Assign a student")
#         print("3. Display enrolled students")
#         print("4. Exit the faculty management system")
#
#         choice = input("Enter your choice (1-4) \n")
#
#         if choice == '1':
#             first_name = input("Enter the first name of the student: ")
#             last_name = input("Enter the last name of the student: ")
#             email = input("Enter the email of the student: ")
#             enrollment_date = input("Enter the enrollment date of the student: ")
#             dob = input("Enter the date of birth of the student: ")
#             new_student = Student(first_name, last_name, email, enrollment_date, dob)
#             faculty.assign_student(new_student)
#         elif choice == '3':
#             faculty.display_enrolled_students()
#
#         elif choice == '4':
#             print("You exited the faculty management system.")
#             break
#
#
# if __name__ == "__main__":
#     main()

class Student:
    def __init__(self, first_name, last_name, email, enrollment_date, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrollment_date = enrollment_date
        self.dob = dob
        self.faculty = None
        self.graduated = False


class Faculty:
    def __init__(self, name, field):
        self.name = name
        self.field = field
        self.students = []


class University:
    def __init__(self):
        self.faculties = []

    def create_faculty(self, name, field):
        new_faculty = Faculty(name, field)
        self.faculties.append(new_faculty)

    def create_student(self, first_name, last_name, email, enrollment_date, dob):
        new_student = Student(first_name, last_name, email, enrollment_date, dob)
        return new_student

    def assign_student_to_faculty(self, student, faculty):
        student.faculty = faculty
        faculty.students.append(student)

    def graduate_student(self, student):
        student.graduated = True

    def display_enrolled_students(self):
        for faculty in self.faculties:
            print(f"Students enrolled in {faculty.name}:")
            for student in faculty.students:
                if not student.graduated:
                    print(student.first_name, ' ', student.last_name)

    def display_graduates(self):
        print("List of graduates:")
        for faculty in self.faculties:
            for student in faculty.students:
                if student.graduated:
                    print(student.first_name, ' ', student.last_name)

    def is_student_in_faculty(self, student, faculty):
        return student.faculty == faculty

    def get_faculty_of_student(self, email):
        for faculty in self.faculties:
            for student in faculty.students:
                if student.email == email:
                    return faculty.name
        return "Student not found."

    def display_all_faculties(self):
        print("List of all faculties:")
        for faculty in self.faculties:
            print(faculty.name)

    def display_faculties_by_field(self, field):
        print("Faculties belonging to: ", field)
        for faculty in self.faculties:
            if faculty.field == field:
                print(faculty.name)

def main():
    university = University()
    while True:
        print("\n1. Faculty Operations:")
        print("   1. Create and assign a student to a faculty")
        print("   2. Graduate a student from a faculty")
        print("   3. Display current enrolled students")
        print("   4. Display graduates")
        print("   5. Check if a student belongs to a faculty")
        print("2. General Operations:")
        print("   1. Create a new faculty")
        print("   2. Search what faculty a student belongs to by the email: ")
        print("   3. Display University faculties")
        print("   4. Display all faculties belonging to a field")
        print("   0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sub_choice = input("Enter sub-choice (1-5): ")
            if sub_choice == "1":
                # Create and assign a student to a faculty
                first_name = input("Enter student's first name: ")
                last_name = input("Enter student's last name: ")
                email = input("Enter student's email: ")
                enrollment_date = input("Enter student's enrollment date: ")
                dob = input("Enter student's date of birth: ")
                faculty_name = input("Enter faculty name: ")
                faculty = next((f for f in university.faculties if f.name == faculty_name), None)
                if faculty:
                    student = university.create_student(first_name, last_name, email, enrollment_date, dob)
                    university.assign_student_to_faculty(student, faculty)
                    print("Student ", first_name, ' ', last_name, "has been assigned to faculty ", faculty_name)
                else:
                    print("Faculty not found.")
            elif sub_choice == "2":
                # Graduate a student from a faculty
                email = input("Enter student's email: ")
                faculty_name = input("Enter faculty name: ")
                faculty = next((f for f in university.faculties if f.name == faculty_name), None)
                if faculty:
                    for student in faculty.students:
                        if student.email == email:
                            university.graduate_student(student)
                            print(student.first_name, ' ', student.last_name, " graduated from ", faculty_name)
                            break
                    else:
                        print("Student not found in the specified faculty.")
                else:
                    print("Faculty not found.")
            elif sub_choice == "3":
                university.display_enrolled_students()
            elif sub_choice == "4":
                university.display_graduates()
            elif sub_choice == "5":
                email = input("Enter student's email: ")
                faculty_name = input("Enter faculty name: ")
                faculty = next((f for f in university.faculties if f.name == faculty_name), None)
                if faculty:
                    student = next((s for s in faculty.students if s.email == email), None)
                    if student:
                        print(student.first_name, '', student.last_name, "belongs to ", faculty_name, ":", university.is_student_in_faculty(student, faculty))
                    else:
                        print("Student not found in the specified faculty.")
                else:
                    print("Faculty not found.")
        elif choice == "2":
            sub_choice = input("Enter sub-choice (1-4): ")
            if sub_choice == "1":
                faculty_name = input("Enter faculty name: ")
                field = input("Enter faculty field: ")
                university.create_faculty(faculty_name, field)
                print("Faculty ", faculty_name, " created.")
            elif sub_choice == "2":
                email = input("Enter student's email: ")
                print(university.get_faculty_of_student(email))
            elif sub_choice == "3":
                university.display_all_faculties()
            elif sub_choice == "4":
                field = input("Enter field: ")
                university.display_faculties_by_field(field)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
