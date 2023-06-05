class Lecture:
    def __init__(self, name, max_students, duration, professors):
        self.name = name
        self.max_students = max_students
        self.duration_minutes = duration
        self.professors = professors
    
    def print_name_and_duration_of_lectures(self):
        print(f"{self.name} is {self.duration_minutes} minutes")

    def add_professors(self, professor):
        self.professors.append(professor)

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def print_full_name(self):
        print(f"{self.first_name} {self.last_name}")

class Student(Person):
    def __init__(self, first_name, last_name, age, lectures):
        super().__init__(first_name, last_name, age)
        self.lectures = lectures
    
    def get_lectures(self):
        for lecture in self.lectures:
            print(f"- {lecture.name}")

    def attend_lecture(self, lecture):
        self.lectures.append(lecture)

    def leave_lecture(self, lecture):
        self.lectures.pop(lecture)

class Professor(Person):
    def __init__(self, first_name, last_name, age, lectures):
        super().__init__(first_name, last_name, age)
        self.lectures = lectures

    def get_lectures(self):
        for lecture in self.lectures:
            print(f"- {lecture.name}")
    
    def teach_lecture(self, lecture):
        self.lectures.append(lecture)

    def remove_lecture(self, lecture):
        self.lectures.pop(lecture)
