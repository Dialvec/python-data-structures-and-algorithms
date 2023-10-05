"""
Python is an object-oriented language. All data items in Python are objects.
Objects that could be thought of as similar are named by a type or class.
"""

"""
Built-in types:
--- int
--- float
--- str
--- list
--- dict
--- tuple
--- set
"""

def declareLiterals():
    x = 5   # int type
    y = 5.0 # float type. Note the '.'
    s = 'Hello world' # string
    l = [ 'Hello' , 'lists'  , 'Python' ] # list
    t = ( 'Hello' , 'tuples' , 'Python' ) # tuple
    w = { 'Hello' , 'sets'   , 'Python' } # set
    d = { 'name': 'Python', 'type': 'Language' , 'version': 3 } # dictionaty 
    
    print( 'x =' , x , 'of type:' , type(x) )
    print( 'y =' , y , 'of type:' , type(y) )
    print( 's =' , s , 'of type:' , type(s) )
    print( 'l =' , l , 'of type:' , type(l) )
    print( 't =' , d , 'of type:' , type(t) )
    print( 'w =' , w , 'of type:' , type(w) )
    print( 'd =' , d , 'of type:' , type(d) )
    

def declareNonLiterals():
    x = 5
    y = float( x )
    s = str(   y )
    l = list(  s )
    t = tuple( l )
    w = set(   t )
    
    print( 'x =' , x , 'of type:' , type(x) )
    print( 'y =' , y , 'of type:' , type(y) )
    print( 's =' , s , 'of type:' , type(s) )
    print( 'l =' , l , 'of type:' , type(l) )
    print( 't =' , t , 'of type:' , type(t) )
    print( 'w =' , w , 'of type:' , type(w) )
    


"""
Classes are custom objects with their own atributes and methods.
Methods are intended to be accesed from outside the class unless declared private as __myPrivateMethod
Accesor methods retrieve atributes but do not modify any class' atributes.
Mutator methods modify the class' atributes
"""

def declareClass():
    
    class Dog:
        # Class' constructor with dog's data
        # self atribute points to the current instance
        # It is useful to declare the attributes' types
        def __init__( self , name: str , day: int , month: int , year: int , bark: str ):
            self.name = name
            self.day  = day
            self.month = month
            self.year  = year
            self.bark = bark

        # Accesor methods
        def getName( self ):
            return( self.name )
        
        # Accesor method that returns a tuple
        def getBirthDate( self ):
            return( ( self.day , self.month , self.year ) )
        
        def getBark( self ):
            return( self.bark )
        
        # Mutator methods
        def setNewName( self , new_name ):
            self.name = new_name
            
        def setNewBark( self , new_bark ):
            self.bark = new_bark
            
        # Operator overload to print the dog using print() function.
        # These operator overloads are also called Magic Methods
        # This method returns a string to use in print()
        def __str__(self) -> str:
            dog_str = "Hi! I'm {0}. I was born on {1}/{2}/{3} and I sound like {4}.".format( self.name , self.day , self.month , self.year , self.bark )
            return( dog_str )
    
    my_dog = Dog( name = 'Fido' , day = 1 , month = 1 , year = 2000 , bark = 'woof' )
    
    print( my_dog )
    print( 'my_dog.getBirthDate() =' , my_dog.getBirthDate() )
    print( 'Renaming my_dog' )
    
    my_dog.setNewName( 'Chuck' )
    
    print( my_dog )


# Launching the equivalent of a main() function in C++
if __name__ == '__main__':
    
    option = 1
       
    while option != '0':
        print( 'Pick a case to display:' )
        print( '( 1 ) Declare literal variables' )
        print( '( 2 ) Declare non-litral variables' )
        print( '( 3 ) Use classes' )
        print( '( 4 ) ' )
        print( '( 0 ) exit' )
        print( '-----' )
        
        option = input( 'Pick a choice: ' )
        
        match option:
            case '1':
                declareLiterals()
            case '2':
                declareNonLiterals()
            case '3':
                declareClass()
            case '4':
                pass
            case '0':
                print( 'Exiting....' )
            case _:
                print( option, '= Invalid option' )
        
        _ = input( 'Press enter to continue.' )
        print( '-'*50 )
        print( '\n' )