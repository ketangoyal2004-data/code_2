class cal:
    def add(self,a,b):
        return a + b

    def sub(self,a,b):
        return a - b
    
    def mul(self,a,b):
        return a * b
    
    def div(self,a,b):
        return a / b
        
obj = cal()
print(obj.add(10,20))
print(obj.sub(10,20))
print(obj.mul(10,20))
print(obj.div(10,20))