'''Create three classes, “Person,” “Employee,” and “Student.” Use multiple
inheritance to create a class “PersonInfo” that inherits from both “Employee” and
“Student.” Add attributes and methods specific to each class.'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee:
    def __init__(self, employee_id, department):
        self.employee_id = employee_id
        self.department = department

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}, Department: {self.department}")

    def work(self):
        print("Employee is working.")


class Student:
    def __init__(self, student_id, major):
        self.student_id = student_id
        self.major = major

    def display_student_info(self):
        print(f"Student ID: {self.student_id}, Major: {self.major}")

    def study(self):
        print("Student is studying.")


class PersonInfo(Person, Employee, Student):
    def __init__(self, name, age, employee_id, department, student_id, major):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, department)
        Student.__init__(self, student_id, major)

    def display_person_info(self):
        self.display_info()
        self.display_employee_info()
        self.display_student_info()


# Example usage:
person_info = PersonInfo("John Doe", 25, "E123", "IT", "S456", "Computer Science")

# Displaying details and specific features of the PersonInfo
print("\nPerson Information:")
person_info.display_person_info()

# Accessing methods from the Employee and Student classes
person_info.work()
person_info.study()
