import python_S_1
class linked:
    class node:
        __slots__='_next','_data'
        def __init__(self,data):
            self._data=data
            self._next=None
    def __init__(self):
        self._size=0
        self._tail=None
    def len(self):
        return self._size
    def is_impty(self):
        return self._size==0
    def len(self):
        return self._size
    def enqueue(self,data):
        new_node=self.node(data)
        if self.is_impty():
            self._tail=new_node
            self._tail._next=self._tail
        else:
            new_node._next=self._tail._next
            self._tail._next=new_node
            self._tail=new_node
        self._size+=1
    def dequeue(self):
        if self.is_impty():
             raise python_S_1.list_is_impty("the list is impty")
        head=self._tail._next
        answer=head._data
        self._tail._next=head._next
        head._data,head._next=None,None
        self._size-=1
        return answer
    def tope(self):
        if self.is_impty():
             raise python_S_1.list_is_impty("the list is impty")
        return self._tail._next._data     
        
    def __str__(self):
        l=[]
        test_node=self._tail._next
        for i in range(self._size):
            l.append(test_node._data)
            test_node=test_node._next
        return f"{l}"
    def reverse(self):
        new_tail=self._tail._next
        self._tail._next=new_tail._next
        new_tail._next=self._tail
        head=new_tail
        for i in range(self._size-2):
            node1=self._tail._next
            self._tail._next=node1._next
            node1._next=head
            head=node1
        self._tail._next=head
        self._tail=new_tail
        return self.__str__()
            
            
        
my_l=linked()
my_l.enqueue(5)
my_l.enqueue(87)
my_l.enqueue("hi")
print(my_l)
my_l.enqueue(941)
my_l.enqueue(112)
my_l.enqueue(982)
print(my_l)
print(my_l.reverse())
#print(my_l)#>>[5, 87, 'hi']
#print(my_l)#>>[]
#my_l.dequeue()>>the list is impty
 
 
    
    
        
             
        
        
        