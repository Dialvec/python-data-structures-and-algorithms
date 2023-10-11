"""
There can be many ways that a particular behavior might be implemented.
We can redefine a function within many classes so it adapt to each class
"""

class Dog:
    
    def __init__( self , name: str , breed: str, bark: str ):
        self.name  = name
        self.breed = breed
        self.bark  = bark

    # These functions will behave diferently depending on the animal
    def makeSound( self ):
        print( self.bark )
        
    def doATrick( self ):
        print( 'Rolling on my belly.... ' )


class Cat:
    
    def __init__( self , name: str , breed: str ):
        self.name  = name
        self.breed = breed

    # These functions will behave diferentle depending on the animal
    def makeSound( self ):
        print(  '  ／)、 Meowww' + '\n' + \
                '（ﾟ､ ｡７ ' + '\n' + \
                'l  ~ヽ    '+ '\n' + \
                'じしf_,)ノ'+ '\n' )
        
    def doATrick( self ):
        print( 'Staring at you o.o ' )
        print( 'Ignoring you -.- ' )
        print( 'Leaving....' )
        
my_dog = Dog( name = 'Fido' , breed= 'Husky' , bark= 'Woof' )
my_cat = Cat( name= 'Antonio Banderas' , breed= 'Spaniard beauty' )

print( '*** Hello Dog ***' )
my_dog.makeSound()
my_dog.doATrick()

print('')
print( '*** Hello Cat ***' )
my_cat.makeSound()
my_cat.doATrick()