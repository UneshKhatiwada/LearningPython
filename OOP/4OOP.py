class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_info(self):
        return f"Name is {self.name}, Age is {self.age} and Grade is {self.grade}"
    def is_passed(self):
        if self.grade >=60:
            return True
        else:
            return False
        
s1 = Student(name="Unesh", age=23, grade=70)
s2 = Student(name="Hari", age=25, grade=40)
s3 = Student(name="Ram", age=21, grade=60)
s4 = Student(name="Sita", age=24, grade=30)
s5 = Student(name="Tina", age=22, grade=80)
s6 = Student(name="Anu", age=23, grade=90)
s7 = Student(name="Nabin", age=25, grade=50)
s8 = Student(name="Bikash", age=21, grade=77)
s9 = Student(name="Ajay", age=24, grade=63)
s10 = Student(name="Anil", age=22, grade=69)

print(s1.get_info())
print(s2.get_info())
print(s3.get_info())
print(s4.get_info())
print(s5.get_info())
print(s10.get_info())
print(s8.get_info())
print(s9.get_info())
print(s7.get_info())
print(s6.get_info())

        