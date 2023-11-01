""" 
Python has another very nice feature called reflection.

Reflection refers to the ability for code to be able to examine attributes about objects
that might be passed as parameters to a function

One interesting aspect of reflection is the ability to see what the type of an object is.
"""

"""
If we write type(obj) then Python will return an object which represents the type of obj.

If obj is a reference to a string, then Python will return the str type object.

if we write str() we get a string which is the empty string. 
writing str() is the same thing as writing “”.

Likewise, writing list() is the same thing as writing [].
"""

""" 
Using reflection we can write one recursive reverse function that will work for strings, 
lists, and any other sequence that supports slicing and concatenation.
"""

def reverseSequence( seq ):
    seq_type = type( seq )
    empty_seq = seq_type()
    
    if seq == empty_seq:
        return empty_seq
    
    return reverseSequence( seq[ 1: ] ) + seq[ 0:1 ]


print( reverseSequence( [1,2,3,4] ) )
print( reverseSequence( 'Hello' ) )