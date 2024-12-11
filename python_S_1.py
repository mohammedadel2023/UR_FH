""" compact array"""
from array import array as ar 
y=ar("i",[2])
y.append(3)
y.append(36)
y2=ar("I",[2,6])
print(y2)
""" y2.append(-5)>ERROR >>can't convert negative value to unsigned int, 
if we use "I" then we cant add a negative to the array because it is unsigned int
"""
y.append(-5)
print(y)#>>array('i', [2, 3, 36, -5])
#############################
""" we can use sys.getsizeof() to find the size of array """
import sys 
print(sys.getsizeof(y))#>>100
################
"""
   CREAT OUR ARRAY "DYNAMIC"
   """
"""
First, here we want to create our own error to
 use later (mentioned in the slides)"""
##########
class index_out(Exception):
    pass
##########
import ctypes #>> to creat the array for the first time and we use it to resize
class my_array:
    def __init__(self):
        self._size_of_array=0
        self._capacity=5#we can choose any number (the capacity of the  first array )
        self._array=self.make_array(self._capacity)
    def make_array(self,c):
        return (c*ctypes.py_object)()
    def resize(self):
        self._capacity=2*self._capacity
        """here if we just add "A" to the array the time complexity for "append"
        it will be O(n) but if we multiply the capacity 
        with 2 or 3 (it will vary(تحتلف in space) the time of adding is O(1)"""
        new_array=self.make_array(self._capacity)
        for i in range (self._size_of_array):
            new_array[i]=self._array[i]
        return new_array    
        
        
    def len(self):
        return self._size_of_array
    def get_item(self,k):
        if not (0<=k<self._size_of_array):
            raise index_out("the index out of the range")#here we use the error we creat above
        return self._array[k]
    def append(self,data):
        if self._capacity==self._size_of_array:
            self._array=self.resize()
        self._array[self._size_of_array]=data
        self._size_of_array+=1
    def __str__(self):#we creat this just to show our result 
        a=[]
        for i in range (self._size_of_array):
            a.append(self._array[i])
        return f"{a}"
my_new=my_array()
my_new.append(56)
my_new.append("kj")
my_new.append(89)
print(my_new.get_item(1))#>>kj
print(my_new)#>>[56, 'kj', 89]
        
        
            
        
     
        
     
        
     
        
     
        
     
        
     