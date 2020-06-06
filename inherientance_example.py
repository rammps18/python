class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks) /len(self.marks)


class workingStudent(Student):
    def __init__(self,name,school,salary):
        super().__init__(name,school)
        self.salary = salary

    

ram = workingStudent('Ram','setupati',80)
print(ram.salary)
ram.marks.append(57)
ram.marks.append(98)
print(ram.average())
                
                   
