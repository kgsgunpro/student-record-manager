class Student:
    def __init__(self,id,name,grade):
        self.id=id
        self.name=name
        self.grade=grade
    def print_details(self):
        print(f'id: {self.id} , name: {self.name} , grade :{self.grade} ')

class Student_manager:
    def __init__(self):
        self.next_id = 1
        self.student_list =[]
        self.student_dict={}
    def add_student(self,name,grade):
        s = Student(self.next_id ,name,grade)
        self.student_dict[self.next_id] = {'name' : name , 'grade':grade}
        self.next_id+=1
        self.student_list.append(s)
        
   
           
sm=Student_manager()
def menu():
    while True:
        inp = int(input('Main menu \n' \
        '1.press 1 to add student :'))
        if inp==1:
            name=input('Enter student name : ')
            grade=input('Enter grade : ')
            sm.add_student(name,grade)


        else:
            break
menu()
            
