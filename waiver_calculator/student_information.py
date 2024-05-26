from student_management import StudentManagement


class StudentInformation(StudentManagement):
    def __init__(self, name, student_id, email, others_information):
        super().__init__(name, student_id, email)
        self.others_information = others_information

    def get_others_information(self):
        return self.others_information

    def course_taken(self):
        return "BSc in CSE"

    def enrollment_record(self):
        return "Summer 21"

    # Overriding get_student_info
    def get_student_info(self):
        return f"Student Information - {super().get_student_info()}"
