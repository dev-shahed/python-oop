from student_management import StudentManagement


class Administrator(StudentManagement):
    def __init__(self, name, student_id, email, accounts):
        super().__init__(name, student_id, email)
        self.accounts = accounts

    def exam_info(self):
        return "Final Exam"

    def accounts_ledger(self):
        return "Accounts Ledger"

    # Overriding get_student_info
    def get_student_info(self):
        return f"Administrator - {super().get_student_info()}"
