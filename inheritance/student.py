from person import Person


class Student(Person):
    def __init__(self, name, age, gender, grade, gpa, roll):
        super().__init__(name, age, gender)
        self.grade = grade
        self.gpa = gpa
        self.roll = roll

    def print_student(self):
        super().print_person()
        print("Student:")
        print("Grade:", self.grade)
        print("GPA:", self.gpa)
        print("Roll:", self.roll)