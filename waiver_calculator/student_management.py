class StudentManagement:
    def __init__(self, name, student_id, email):
        self.name = name
        self.id = student_id
        self.email = email

    def get_student_info(self):
        return f"Name: {self.name}, ID: {self.id}, Email: {self.email}"

    def course_information(self):
        return "Course Information"

    def result(self):
        return "Result"
