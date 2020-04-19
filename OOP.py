class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    avg = lambda self: sum(self.grades) / len(self.grades)
    
new_student = Student("Tim", [3,4,5,6])