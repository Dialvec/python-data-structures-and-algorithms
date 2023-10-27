""" 
Scope refers to a part of a program where a collection of identifiers are visible.

When a program is executing a line of code, the scope that surrounds that line of code is called the local scope.

When you reference an identifier in a statement in your program, Python first examines the local scope to see if 
the identifier is defined there, within the local scope.
"""

""" 
An identifier, x, is defined under one of three conditions.
• A statement like x = … appears somewhere within the current scope. 
    In this case id would be a reference to an object in the local scope.
• x appears as a parameter name of the function in the current scope. 
    In this case x would be a reference to an object that was passed to the current function as an argument.
• x appears as a name of a function or class through the use of a function def or class definition within the current scope.
"""

""" 
If Python does not find the reference id within the local scope, it will examine the Enclosing scope to see if it can find x there.

Which scope is local is determined by where your program is currently executing.

Scopes are nested. This means that each scope is nested inside another scope.

The final enclosing scope of a module is the module itself.
"""

""" 
Each scope has its own copy of identifiers. 

The choice of which value is an identifier pointing to is made by always selecting the innermost scope that defines the identifier.

If we use an identifier that is already defined in an outer scope, we will no longer be able to access it from an inner scope 
where the same identifier is defined.

The scope never includes the function name itself, but includes its parameters and the body of the function.
"""

"""
Using Python it is possible to define variables at the Global level. Generally this is a bad programming practice. Avoid it

Using too many global variables will generally lead to name conflicts and will likely lead to unwanted side effects.

Poor use of global variables contributes to spaghetti code which is named for the big mess it takes to untangle it to figure out what it does.
"""

"""
The final scope in Python is the Built-In scope.

If an identifier is not found within any of the nested scopes within a module 
and it is not defined in the global scope, Python will examine the built-in identifiers to see if it is defined there.

Consider the asignation:
x = int("6")

Python would first look in the local scope to see if int were defined as a function or variable within that local scope. 

If int is not found within the local scope, Python would look in all the enclosing scopes 
starting with the next inner-most local scope, working outwards from there. 

If not found in any of the enclosing scopes, Python would then look in the global scope for the int identifier.

If not found there, then Python would consult the Built-In scope, where it would find the int class or type.
"""

""" 
Mark Lutz, in his book Learning Python described the rules of scope in Python programs using the LEGB acronym.
(L)ocal
(E)nclosing
(G)lobal
(B)uilt-in
"""

"""
The parameters and body of each function define a scope within a Python program.

The parameters and variables defined within the local scope of a function must be stored someplace within the computer's RAM.

Python splits the RAM up into two parts called the Run-time Stack and the Heap.

The run-time stack is a stack of Activation Records.
The Python interpreter pushes an activation record onto the run-time stack when a function is called.
When a function returns the Python interpreter pops the corresponding activation record off the run-time stack.

Python stores the identifiers defined in the local scope in an activation record.
When a function is called, a new scope becomes the local scope. At the same time a new activation record is pushed onto the run-time stack.
This new activation record holds all the variables that are defined within the new local scope.
When a function returns its corresponding activation record is popped from the run-time stack.

The Heap is the area of RAM where all objects are stored.
When an object is created it resides in the heap. 
The run-time stack never contains objects.
References to objects are stored within the run-time stack and those references point to objects in the heap.
"""

def scopes():
    # Here we start the enclosing scope of the function
    # We will play with various scopes for an identifier called x
    
    # Let's define a function called printX just to save up some time
    # The identifier x inside the scope of the printX function points to
    #   the value we pass as parameter when we invoque the function.
    #   Isolated from any other identifier called x in the outer scopes
    def printX( x ) -> None:
        print( 'Value of x =' , str(x) , 'of type' , type(x) )
    
    
    # We are now out of the printX function scope
    # Back to the enclosing scope
    # Start with a basic asignation
    x = True
    printX( x )
    
    # Reasign the x in the enclosing scope
    x = 'Hello scopes'
    
    #Declare a new function using x
    def mutateX( x ):
        print( 'Mutating x' )
        printX( x )
        # We look for the type of value x points to and reasign x afterwards
        
        if isinstance( x , int ):
            x = 'Hello mutate'
        elif isinstance( x , str ):
            x = 5
        elif isinstance( x , list ):            
            x = True
        elif isinstance( x , bool ):
            x = []
        else:
            print('Unknown class')
        
        print( 'After mutation' )
        printX( x )
        return( x )
    
    print('********')
    print('Back to enclosing scope')
    print( 'Calling mutate X without reasigning the enclosed scope identifier' )
    mutateX( x )
    print( 'Enclosed scope x:' )
    printX( x )
    print('********')
    print( 'Calling mutate X reasigning the enclosed scope identifier' )
    x = mutateX( x )
    print( 'Enclosed scope x:' )
    printX( x ) 
    

scopes()