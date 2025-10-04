class overload:
    def __init__(self,x):
        self.a = x
    def __lt__(self,other):
        if self.a < other.a:
                return self.a,"is less than",other.a
        else:
                return self.a,"is not less than",other.a
        
    def __eq__(self,other):
        if self.a == other.a:
                return self.a,"is equal to",other.a
        else:
                return self.a,"is not equal to",other.a
        
obj1 = overload(12)
obj2 = overload(45)
print(obj1 < obj2)
print(obj1 == obj2)        
        
      