#classes
class Human:
    def __init__(self,name,last_name):
        self.name = name
        self.last_name = last_name

    def full_name(self):
        return self.name +  self.last_name
    
    def __str__(self):
        return self.name + 'object'

class Employee(Human):
    manager = 'Hasan'

    def programer(self):
        print('I am a web developer')

p1 = Employee('ali' , 'bigdeli')
p2 = Employee("hasan" , 'hassani')


print(p1)
print(p2.manager)
p1.programer()