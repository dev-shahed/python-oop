from person import Person
from student import Student
from teacher import Teacher


def main():
    t1 = Teacher("Nurul Islam", 40, "Male", "Chemistry", "BSc", 23123424, 10000)
    t1.print_teacher()

    s1 = Student("Shahed", 15, "Male", "Ten", 5.00, 2)
    s1.print_student()

    # Checking instances
    print("\nKnowing instance:")
    p1 = Person("SA", 10, "Male")
    print(p1.__dict__)

    print(isinstance(t1, Person))  # True
    print(isinstance(s1, Person))  # True
    print(isinstance(p1, Student))  # False

if __name__ == "__main__":
    main()