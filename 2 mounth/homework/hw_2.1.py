class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Добрый день! Меня зовут {self.full_name}, мне {self.age} и я {self.is_married}")

class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def average_rate(self):
        sum_rates = sum(self.marks.values())
        count = len(self.marks)
        average = sum_rates / count
        average = round(average, 1)
        print(f"Средняя оценка студента {student_1.full_name} по предметам {student_1.marks}: {average}")

class Teacher(Person):
    base_salary = 50000
    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def bonus_salary(self):
        bonus = 0
        if self.experience > 3:
            bonus_years = self.experience - 3
            bonus = bonus_years * 0.05 * self.base_salary
        full_salary = self.base_salary + bonus
        return full_salary

def create_students():
    stud1 = Student("Miguel", 19, "не женат", {"Algebra": 3, "Literature": 2, "Geography": 5})
    stud2 = Student("Mireille", 15, "не замужем",{"Algebra": 5, "Literature": 5, "Geography": 3})
    stud3 = Student("Marlis", 22, "не женат",{"Algebra": 3, "Literature": 3, "Geography": 5})
    list_students = [stud1, stud2, stud3]
    for student in list_students:
        sum_rates = sum(student.marks.values())
        count = len(student.marks)
        average = sum_rates / count
        average = round(average, 1)
        print(f"Студент {student.full_name}, {student.age} лет. Оценки по предметам: {student.marks},"
              f" а средняя оценка: {average}")

    return list_students

person_1 = Person("Miguel", "19", "не женат")
person_1.introduce_myself()

student_1 = Student("Mirey", "15", "не замужем", {"Algebra": 4, "Literature": 5, "Geography": 4})
student_1.average_rate()

teacher_1 = Teacher("Marsel", "22", "женат", 10)
print(f"Зарплата учителя {teacher_1.full_name}, который {teacher_1.is_married} "
      f"и которому {teacher_1.age} года - {teacher_1.bonus_salary()} сом")

students = create_students()


