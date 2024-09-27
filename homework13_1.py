class StudentCountError(Exception):
    def __init__(self, message="Не можна додавати більше студентів"):
        self.message = message
        super().__init__(self.message)

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'His/her name is {self.first_name}{self.last_name}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book
    def __str__(self):
        return f'{super().__str__()} and his/her record book number is {self.record_book}'

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        try:
            if len(self.group) >= 10:
                raise StudentCountError()
            self.group.add(student)
        except StudentCountError as e:
            print(e.message)


    def delete_student(self, last_name):
        student_to_remove = self.find_student(last_name)
        if student_to_remove:
            self.group.remove(student_to_remove)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None


    def __str__(self):
        all_students = [Student('Male', 30, f'Steve{i}', f'Jobs{i}', f'AN1{i}') for i in range(3, 12)]
        return f'Number:{self.number}\\n {all_students} '

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st4 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st5 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st6 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st7 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st8 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st9 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st10 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st11 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st12 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
gr.add_student(st11)
gr.add_student(st12)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)

gr.delete_student('Taylor')