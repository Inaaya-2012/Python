class person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def disp(self):
        print(f'My name is {self.name} and my id is {self.id}') 

class employee:
    def __init__(self,name,id,salary,post):
        person.__init__(self,name,id)
        self.salary = salary
        self.post = post
    def display(self):
        person.disp(self)
        print(f'My salary is {self.salary} and my designation is {self.post}')

emp1 = employee('Kelly',"678910",'80000','Manager')
emp1.display()                       