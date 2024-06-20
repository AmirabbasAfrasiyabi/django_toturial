#classes
class Human:
    def __init__(self,name,last_name):
        self.name = name
        self.last_name = last_name
    def full_name(self):
        return self.name +  self.last_name
p1 = Human('ali' , 'bigdeli')
p2 = Human("hasan" , 'hassani')

# p1.name = 'ali'
# p1.lastname = 'bigdeli'

# p2.name = 'amirabbas'
# p2.lastname = 'afrasiyabi'
# p2.email = 'abb.afrasiyabi@gmail.com'

print(p1.name )
# p2.management = 'atiye'
# print(p2.management)
print(p2.name)

print(p1.full_name())
print(p2.full_name())
