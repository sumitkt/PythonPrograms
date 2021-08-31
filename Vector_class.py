class Vector:
    """ Multidimensional vector space"""
    def __init__(self,d):
        """ creates d dimensional vector of zeros"""
        self._coords=[0]*d

    def __len__(self):
        """ Return the dimension of the vector"""
        return len(self._coords)

    def __getitem__(self, j):
        """ Return the jth cordinate of vector"""

        return self._coords[j]

    def __setitem__(self, key, value):
        """set j th cordinate to  a value"""
        self._coords[key]=value

    def __add__(self, other):
        """ return the sum of the two vectors"""
        if len(self)!=len(other):
            raise ValueError('dimension must agree')
        result=Vector(len(self))         #start with vector of zeros
        for j in range(len(self)):
            result[j]=self[j]+other[j]
        return result

    def __eq__(self,other):
        """ Return true if vector has some coordinate as other """
        return self._coords == other._coords
        #print(type(self))
        #print(type(self._coords))
        #return self==other

    def __ne__(self, other):
        """ Return true if vectors differs from other """
        return not self==other      # rely on existing __eq__ definition

    def __str__(self):
        """ Produce string representation  of vector """
        return '<'+str(self._coords)[1:-1]+'>'



v1=Vector(3)
v2=Vector(3)

for i in range(v1.__len__()):
    v1.__setitem__(i,i*3)
    v2.__setitem__(i,i*5)

for i in range(v1.__len__()):
    print(v1.__getitem__(i),end=' ')
    print(v2.__getitem__(i))
    print()
if v1.__eq__(v2):
    print("True")
else:
    print("False")

v3=v1.__add__(v2)
print(v3.__str__())