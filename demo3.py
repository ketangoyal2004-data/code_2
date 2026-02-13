class std:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

    def course(self,course):
        self.course = course
        print("Course:",self.course)

    def branch(self,branch):
        self.branch = branch
        print("Branch:",self.branch)    

obj = std("Harry",20)
obj.display()   
obj.course("Python")    
obj.branch("CSE")