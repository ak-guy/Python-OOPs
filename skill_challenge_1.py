# # skill challenge - 1

import random
class Student:
    educational_platform = "Udemy"

    def __init__(self, name, age=23):
        self.name = name
        self.age = age

    def greet(self):
        greetings = [f"Hi i am ...{self.name}", f"Hey there my name is ...{self.name}", f"Hi oh my name is ... {self.name}"]
        return random.choice(greetings)


if __name__ == '__main__':
    student_list = ["Shivam", "Thakur", "Sabrina", "Avantika"]

    class_Student_object_list = [Student(student_name) for student_name in student_list]
    for greetings in class_Student_object_list:
        print(greetings.greet())