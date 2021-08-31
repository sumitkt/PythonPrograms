#####class methods############
class Employee:

    no_of_leaves=34

    def __init__(self,e_name,e_doj,e_dob):
        self.name=e_name
        self.doj=e_doj
        self.dob=e_dob

    @classmethod
    def change_no_of_leaves(cls,leaves):
        cls.no_of_leaves=leaves

    #here i will be using class method as alternative constructor....this will create a instance of this class
    @classmethod
    def create_instance(cls,string):
        return cls(*string.split('_')) ## or we can do: parameters=string.split('_') and then cls(parameters[0],parameters[1],parameters[2])


suresh=Employee('suresh','22/10/20','4-06-1990')
ramesh=Employee('ramesh','22/10/20','4-06-1990')

karan=Employee.create_instance('karan_1_1998')

print(karan.__dict__)