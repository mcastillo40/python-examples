class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grades = []

    def avg(self):
        return sum(self.grades) / len(self.grades)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    # No argument method used as a property
    @property
    def weekly_salary(self):
        return self.salary * 40


new_student = WorkingStudent("Tim", 'MIT', 15.50)
new_student.grades.append(12)
new_student.grades.append(55)

print(new_student.avg())


class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    # Don't use most of the time
    @staticmethod
    def from_sum(value1, value2):
        return FixedFloat(value1 + value2)

    @classmethod
    def from_sum_class(cls, value1, value2):
        return cls(value1 + value2)


new_num = FixedFloat.from_sum(19.575, 0.789)
print(new_num)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'


new_euro = Euro(18.786)
print(new_euro)

new_euro = Euro.from_sum(16.758, 9.999)
print(new_euro)

new_euro = Euro.from_sum_class(16.758, 9.999)
print(new_euro)