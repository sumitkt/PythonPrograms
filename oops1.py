# it follows trhe concept of DRY
# DRY:Do not Repeat Yourself

#print('&'.join(['sumit','kumar','Thakur']))

# we can have list of functions  that are waiting to be executed

#######################OOPS###########################
class Student:
    school='DBHS'
    pass



obj1=Student()
obj2=Student()

obj1.name="sumit"
obj2.name="kumar"
print(Student.__dict__)
print((obj1.__dict__))
print(type(obj2.name))