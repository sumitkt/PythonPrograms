##### class ###########
from datetime import datetime


class Employee:

    def __init__(self, ename, edoj, edob):
        self.name = ename
        self.date_of_joining = datetime.strptime(edoj, '%d/%m/%y')
        self.date_of_birth = datetime.strptime(edob, '%d-%m-%Y')

    pass


suresh = Employee('Suresh', '22/10/20', '4-06-1990')

print(suresh.date_of_birth)
