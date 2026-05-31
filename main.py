class Student_manager:
    def __init__(self):
        self.next_id = 1
        self.student_dict={}
    def add_student(self,name,grade):
        
        self.student_dict[self.next_id] = {'name' : name , 'grade':grade}
        self.next_id+=1
        
    def show_student(self,student_id):
        name=self.student_dict[student_id]['name']
        grade=self.student_dict[student_id]['grade']
        return f'id: {student_id} , name: {name} , grade :{grade} '
    
           
sm=Student_manager()
def menu():
    while True:
        try:
            inp = int(input('Main menu \n' \
            '1.press 1 to add student \n'
            '2.press 2 to fetch details of student'
            'press any number to exit'))
            if inp==1:
                name=input('Enter student name : ')
                grade=input('Enter grade : ')
                sm.add_student(name,grade)

                print(f'the follwing details added to database \n {sm.show_student(sm.next_id -1)}')
            elif inp==2:
                try :
                    student_id = int(input('Enter student id'))
                    print(sm.show_student(student_id))
                except Exception as e:
                    print('id doesn\'t exist ', e ,type(e))
            else:
                break
        except:
            print('please enter integer')
menu()
            
