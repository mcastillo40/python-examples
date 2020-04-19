class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def avg(self):
        return sum(self.grades) / len(self.grades)

    def __len__(self):
        return len(self.grades)

    def __repr__(self):
        return f'Student with {len(self)} grades'

    def __getitem__(self, item):
        return self.grades[item]


new_student = Student("Tim", [3, 4, 5, 6])

print(new_student.avg())
print(new_student)
print(new_student[2])
