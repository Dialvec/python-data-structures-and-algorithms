import datetime

"""
Now we will explore the efficiency of doing the same operation in different ways
and connect with the Big-Oh notation

Let's start by declaring a class called PyList and create its own append method
"""

class PyList:
    def __init__( self ) -> None:
        self.items = []
        
    # Its own mutator append method... maybe not the most efficient
    def append( self , new_item ):
        self.items = self.items + [ new_item ]
        
""" 
This code appends new item to its items list as follows:
1. The new item is made into a one-element list by putting [] around it.
    So we create a new element in memory that points to new_item's value.
2. PyList's items list is concatenated with the new one-element list using the + operator.
    The concatenation result is stored in a new memory space.
3. The assignment of the concatenation result to self.items updates the PyList items object. 
    So it now refers to a new list 
"""
"""
The first time the append method is called, there are 0 elements in the *self.items* list and 1 element in the [ new_item ] list. 
    So the append method must access 1 element of a list to form the concatenated list, which will have a total of 1 element in it.
The second time the append method is called, there is 1 element in the *self.items* list and 1 element in the [ new_item ] list. 
    So the append method must access 2 elements to form the new list.
The third time the append method is called, a total of three elements must be accessed to form the concatenated list.
So on, when the *n-th* element is appended to the sequence there will have to be *n* elements copied to form the new list.
"""
""" 
How does this append method perform as the size of the PyList grows?
"""
"""
The first time the append method is called, there are 0 elements in the *self.items* list and 1 element in the *[ new_item ]* list. 
    So the append method must access 1 element of a list to form the concatenated list, which will have a total of 1 element in it.
The second time the append method is called, there is 1 element in the *self.items* list and 1 element in the *[ new_item ]* list.
    So the append method must access 2 elements to form the new list.
The third time the append method is called, a total of 3 elements must be accessed to form the concatenated list.
"""
""" 
So on, in order to make it up to the n-th append operation, there will have to be n elements copied to form the new list.
"""
"""
If we want to calculate the amount of time it takes to append *n* elements to the *PyList* we would have to:
- Add up all the list accesses and multiply them by the amount of time it takes to access a list element
- Add the time it takes to store a list element.

So, we can state that the amount of time to append n elements can be written as: f(n) = 1 + 2 + ... + n

The summation can be rewritten as f(n) = n(n+1)/2 = (n^2 + n)/2

It is seen that for a given n, the highest power of n in the f(n) expression is n^2.
    So we conclude that the current PyList append method exhibits O(n^2) complexity, which is not a desired performance.
"""
"""
In terms of big-Oh notation we say that the append method is O(n^2).
"""
"""
You typically want to stay away from writing code that has this kind of computational complexity associated with it
unless you are absolutely sure it will never be called on large data sizes.
"""
"""
The use of the + operator is what causes Python to access each element of that first list.
When + is used a new list is created with space for one more element.
Then all the elements from the old list must be copied to the new list and the new element is added at the end of this list.
"""
""" 
Using the append method on lists changes the code to use a mutator method to alter the list by adding just one more element.
It turns out that adding one more element to an already existing list is very efficient in Python.

Appending an item to a list using the append command is a O(1) operation.
This means that to append $n$ items to a PyList we have gone from O(n^2) to O(n) complexity by using the built-in append operation
instead of the initially declared append function.
"""

class EfficientPyList:
    def __init__( self ) -> None:
        self.items = []
        
    # A more efficient append method
    def append( self , new_item ):
        self.items.append( new_item )



class AmortizedPyList:
    # size = 1 is the initial number of locations for the list object.
    # num_items tracks how many elements are currently stored since self.items may have empty locations
    def __init__( self , size = 1 ) -> None:
        self.items = [None] * size
        self.num_items = 0

    def append( self , new_item ):
        # If there is no free space in the items list for the new item
        if self.num_items == len( self.items ):
            # Make the list bigger by allocating a new list twice the current size
            # Copy all the elements over to the new list
            new_list = [ None ]*( self.num_items*2 )
            
            for index in range( len( self.items ) ):
                new_list[ index ] = self.items[ index ]
                
            self.items = new_list
        
        self.items[ self.num_items ] = new_item
        self.num_items += 1

def testAppendMethods():
    
    pylist = PyList()
    better_pylist = EfficientPyList()
    amort_pylist  = AmortizedPyList()
    
    n_min = 10
    n_max = 100000
    
    start_time = datetime.datetime.now()
    
    for _ in range( n_min , n_max , 10 ):
        pylist.append( datetime.datetime.now() )
    pylist.items = [ ( x - start_time).microseconds for x in pylist.items ]
    
    start_time = datetime.datetime.now()
    
    for _ in range( n_min , n_max , 10 ):
        better_pylist.append( datetime.datetime.now() )
    better_pylist.items = [ ( x - start_time).microseconds for x in better_pylist.items ]
    
    start_time = datetime.datetime.now()
    
    for _ in range( n_min , n_max , 10 ):
        amort_pylist.append( datetime.datetime.now() )
    amort_pylist.items = [ ( x - start_time).microseconds for x in amort_pylist.items if type( x ) == datetime.datetime ]
    
    print( 'List size | inefficient | efficient | amortized' )
    for n in range( len( pylist.items ) ):
        print( 'n = ' , str( (n + 1)*10 ) , ' |' , str( pylist.items[n] ) , 'us |' , str( better_pylist.items[n] ) , 'us |' , str( amort_pylist.items[n] ) , 'us' )
    print( 'List size | inefficient | efficient | amortized' )
        

testAppendMethods()