list_t = [1,2,3,4,4,5,5,5]
set_t = set(list_t)
print(list_t,set_t)
set_t.add(6)
set_t.add(7)
set_t.remove(3)
print(list_t,set_t)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set2 - set1)
print(set1 ^ set2)

#dictionary

dict ={'key':'value','name':'ali', 'last_name':'afrasiyabi'}
dict['name'] = 'amirabbas'
print(dict['name'])

#get
print(dict.get('last_name')) 

#update
dict.update({'name':'amirabbas', 'last_name':'mohammadi'})

print(dict['name'])
print(dict.get('last_name')) 


