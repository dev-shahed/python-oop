from person import Person
from student import Student
from teacher import Teacher


def main():
    t1 = Teacher("Nurul Islam", 40, "Male", "Chemistry", "BSc", 23123424, 10000)
    t1.print_teacher()

    s1 = Student("Shahed", 15, "Male", "Ten", 5.00, 2)
    s1.print_student()

if __name__ == "__main__":
    main()