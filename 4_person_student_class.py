class Person:
    def introduce(self):
        print('I am Person')

class Student(Person):
    def introduce(self):
        print('I am Student')


student1 = Student()
student1.introduce()