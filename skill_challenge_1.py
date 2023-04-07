#################
## CHALLENGE 1 ##
#################

# Requirements
# - Define a Student class with 2 instance attributes (name, age) and 1 class attribute (educational_platform = udemy);
# - Make it so that instances of Student could be created by simply specifying the name. Hint: set the default age to a number
# - Define a greet() method which alternates between various name greetings. When invoked, the method should randomly select
# a greeting and interpolate in the name of the student
#        - Hi, I'm...
#        - Hey there, my name is...
#        - Hi. Oh, my name is...
# - Starting with a list of several student names, create student instances from each, and have each student introduce themselves


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