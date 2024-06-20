#classes
class Human:
    def __init__(self,name,last_name):
        self.name = name
        self.last_name = last_name
    def full_name(self):
        return self.name +  self.last_name
    
    def __str__(self):
        return self.name + 'object'

p1 = Human('ali' , 'bigdeli')
p2 = Human("hasan" , 'hassani')


print(p1)
print(p2.full_name())
