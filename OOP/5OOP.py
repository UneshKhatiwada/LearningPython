class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum +=val
        print("Hi", self.name,", Your average score is:", sum/3)


s1 = Student("Tony Stark", [99,98,97])
s2 = Student("Captian America", [89, 88, 87])
s1.get_avg()
s2.get_avg()

