from administrator import Administrator
from exam_controller import ExamController
from student_information import StudentInformation
from student_management import StudentManagement


def main():
    # Create instances
    admin = Administrator("Admin", 1, "admin@gmail.com", 12345)
    student_info = StudentInformation("Rubaiyat Ferdousi", 111, "rubacse21@gmail.com", "From Bogura")
    exam_controller = ExamController(3.8, 12)
   

     # Print student information
    print(student_info.get_student_info())
    print(f"District: " + student_info.get_others_information())
    print(f"Course taken: " + student_info.course_taken())
    print(f"Enrolled: " + student_info.enrollment_record())
    print("\n")

    # Calculate tuition fee after waiver
    base_fee = 10000
    waived_fee = exam_controller.calculate_tuition_fee(base_fee)
    print(f"Base Tuition Fee: {base_fee}")
    print(f"Waived Tuition Fee: {waived_fee}")

if __name__ == "__main__":
    main()
