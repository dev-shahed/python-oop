from person import Person


class Teacher(Person):
    def __init__(self, name, age, gender, subject, qualification, phone, salary):
        super().__init__(name, age, gender)
        self.subject = subject
        self.qualification = qualification
        self.phone = phone
        self._salary = salary

    def print_teacher(self):
        super().print_person()
        
        print("Teacher:")
        print("Subject:", self.subject)
        print("Qualification:", self.qualification)
        print("Phone:", self.phone)
        print("Salary:", self._salary)

    # Getter for salary
    @property
    def salary(self):
        return self._salary

    # Setter for salary
    @salary.setter
    def salary(self, salary):
        self._salary = salary
