class Student:
    def __init__(self,id,name,grade):
        self.id=id
        self.name=name
        self.grade=grade
    def print_details(self):
        print(f'id: {self.id} , name: {self.name} , class :{self.grade} ')
s1=Student(1,'ravi',10)
s2=Student(2,'ram',9)
s1.print_details()
