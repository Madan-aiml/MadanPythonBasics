class Student:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks

    def get_average(self):
        return sum(self.marks) / len(self.marks)
s1 = Student("Madan",[90,85,88,99,89])
print("Name:",s1.name)
print("Average:", s1.get_average())
