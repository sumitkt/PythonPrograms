class SequenceIterator:
    """ An iterator for any of Python's sequence types"""

    def __init__(self,sequence):
        """ create an iterator for the given sequence """
        self._seq=sequence      #keep a refrence to the under_lying data
        self._k=-1            #will increment to zero on first call

    def __next__(self):
        """ return the next element of the sequence or else raise Stop iteration error"""
        self._k+=1          # move to next index
        if self._k<len(self._seq):
            return (self._seq[self._k]) #  return the element
        else:
            raise StopIteration()



iter1=SequenceIterator('sumit')
#print(iter1.__next__())
while i<iter


