#list
L1 = ["Ali", "Bigdeli",27,1,2,3,4,5,6,['hello',1,2,3]]    
L2 = [1, 2, 3, 4, 5, 6]  
print(L1)
print(L2)
print(L1[0])
print(L2[0])
print(L1[-1])
print(L2[-1])
L1[0] = 14
print(L1)
L1.append("abbas")
print(L1)
L2.insert(1,"abbas")
print(L2)

#slice
print(L1 [2:])
#tuple
t1 = (1,2,3,4,5,6)
print(type(t1))
print(t1)

tuple_t = tuple(L1)
print(tuple_t)
