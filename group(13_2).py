class StudentCountError(Exception):
    def __init__(self, message="Не можна додавати більше студентів"):
        self.message = message
        super().__init__(self.message)

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
        return f'Group number: {self.number}, Students: {[str(student) for student in self.group]}'
