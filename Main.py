
class Student:
    total_students = 0

    def __init__(self, student_id, name, course, progress=0):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.progress = progress
        Student.total_students += 1

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Learning Progress: {self.progress}%")
        print("-" * 30)

    def update_progress(self, new_progress):
        if 0 <= new_progress <= 100:
            self.progress = new_progress
            print("Learning progress updated successfully.")
        else:
            print("Progress must be between 0 and 100.")

    @classmethod
    def get_total_students(cls):
        return cls.total_students


class LearningPortal:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        for existing in self.students:
            if existing.student_id == student.student_id:
                print("A student with this ID already exists.")
                return

        self.students.append(student)
        print(f"{student.name} has been added successfully.")

    def display_students(self):
        if not self.students:
            print("No student records are available.")
            return

        print("\nSTUDENT LEARNING PORTAL")
        print("=" * 30)

        for student in self.students:
            student.display_info()

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None


def main():
    student1 = Student("ST001", "Abdul Kamara", "Diploma in IT", 60)
    student2 = Student("ST002", "Fatmata Sesay", "Diploma in IT", 75)
    student3 = Student("ST003", "Ibrahim Conteh", "Diploma in IT", 40)

    portal = LearningPortal()

    portal.add_student(student1)
    portal.add_student(student2)
    portal.add_student(student3)

    portal.display_students()

    print("\nSEARCH RESULT")
    student = portal.find_student("ST002")

    if student is not None:
        student.display_info()
    else:
        print("Student not found.")

    student1.update_progress(80)

    print("\nUPDATED STUDENT RECORD")
    student1.display_info()

    print("Total Student objects created:",
          Student.get_total_students())


if __name__ == "__main__":
    main()
