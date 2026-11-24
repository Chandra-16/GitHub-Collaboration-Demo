class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
    def display(self):
        print("Student name: ", self.name)
        print("Student Roll Number: ", self.roll_number)

student = Student("Prabhath", 101)
student.display()        