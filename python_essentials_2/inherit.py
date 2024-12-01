class Super:
    superVar = 1
    
class Sub(Super):
    subVar = 2
   
obj1 = Sub()
print(obj1.subVar, obj1.superVar) 
print(Sub.__bases__)
# & you thought that class vars aren't accessible to the objects ? really? 


# properties: instance variables.
class Super2:
    def __init__(self):
        self.supVar = 11


class Sub2(Super2):
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj2 = Sub2()

print('obj 2 dict', obj2.__dict__)
print(obj2.subVar)
print(obj2.supVar)
# * instance variables from super classes need to init. Simple enough?
    