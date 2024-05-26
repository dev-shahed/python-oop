class ExamController:
    def __init__(self, cgpa, duration):
        self.cgpa = cgpa
        self.duration = duration

    def result(self):
        return "Result"

    def exam_details(self):
        return "Exam Details"

    def calculate_tuition_fee(self, base_fee):
        if self.cgpa > 3.75:
            discount = 0.25
        elif self.cgpa > 3.5:
            discount = 0.20
        else:
            discount = 0
        waived_fee = base_fee * (1 - discount)
        return waived_fee
