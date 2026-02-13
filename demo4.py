class std:
    def std_name1(self,name):
        self.name = name
        return self.name

    def std_name2(self,name):   
        self.name = name
        return self.name
    
obj = std()
print(obj.std_name1("Harry"))
print(obj.std_name2("Darry"))