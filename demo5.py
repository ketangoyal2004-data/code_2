class name:
    def name1(self,name):
        self.name = name
        return self.name
    
    def name2(self,name):
        self.name = name
        return self.name
    
obj = name()  
print(obj.name1("Harry"))
print(obj.name2("Darry"))