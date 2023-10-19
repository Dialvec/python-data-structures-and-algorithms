"""
XML stands for eXtensible Markup Language.
XML is a meta-language for data description.
"""

"""
An XML document begins with a special line to identify it as an XML file. Like this.
<?xml version="1.0" encoding="UTF-8"?>
"""

"""
The rest of an XML file consists of elements or nodes. 
Each node is identified by a tag or a pair of beginning and ending tags. 
Each tag is delimited by angle brackets.

<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<Element>
    ... Some data here
</Element>

The slash just before the tag name means that it is a closing tag.
"""

"""
Each XML element may have attributes specifically mapped for the destination command.

<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<ContainerTag>
    <Element>
        <key1>Value 1</key1>
        <key2>Value 2</key2>
        .
        <keyn>Value n</keyn>
    </Element>
    <Element>
        <key1>Value A</key1>
        <key2>Value B</key2>
        .
        <keyn>Value N</keyn>
    </Element>
</ContainerTag>
"""

"""
Let's write our Cat and Dog classes in XML format
Let's take advantage of polymorphism and method overloading to get teh xml representation via the __str__ method
"""

# minidom will be user later for reading XML files
# Be carefull when using the 'as' command to avoid overwriting function or varaibles names!!!!!
import os
import xml.dom.minidom as minidom

HERE = os.path.dirname(__file__)

class Dog:
    
    def __init__( self , name: str , breed: str, bark: str ):
        self.name  = name
        self.breed = breed
        self.bark  = bark

    def makeSound( self ):
        print( self.bark )
        
    def doATrick( self ):
        print( 'Rolling on my belly.... ' )
        
    def sayHi( self ):
        print( 'Hi! My name is ' + self.name + ' and I am a ' + self.breed + " doggo... " + self.bark + '!' )
    
    def __str__(self) -> str:
        xml_str = '<Dog>\n' + \
                    '\t<name>'  + self.name  + '</name> \n' + \
                    '\t<breed>' + self.breed + '</breed>\n' + \
                    '\t<bark>'  + self.bark  + '</bark> \n' + \
                  '</Dog>\n'
        return xml_str


class Cat:
    
    def __init__( self , name: str , breed: str ):
        self.name  = name
        self.breed = breed

    def makeSound( self ):
        print(  '  ／)、 Meowww' + '\n' + \
                '（ﾟ､ ｡７ ' + '\n' + \
                'l  ~ヽ    '+ '\n' + \
                'じしf_,)ノ'+ '\n' )
        
    def doATrick( self ):
        print( 'Staring at you o.o ' )
        print( 'Ignoring you -.- ' )
        print( 'Leaving....' )
    
    def sayHi( self ):
        print( "I'm " + self.name + '. Praise me hooman!' )
        
    def __str__(self) -> str:
        xml_str = '<Cat>\n' + \
                    '\t<name>'  + self.name  + '</name> \n' + \
                    '\t<breed>' + self.breed + '</breed>\n' + \
                  '</Cat>\n'
        return xml_str


def writeXMLAnimals():
    fido = Dog( 'Fido' , 'Husky' , 'woof')
    mimi = Cat( 'Mimi' , 'Fuzzy')
    print( fido )
    print( mimi )



"""
To read XML files, existing parsers can leverage the grammar load as XML is an standardized language.
The minidom parser reads an entire XML file by calling the parse method on it. 
It places the entire contents of an XML file into an sequence of Element objects. 
"""

def createXMLDog( attr: list ) -> Dog:
    
    for dom_element in attr:
        
        match dom_element.tagName:
            
            case 'name':
                name = dom_element.firstChild.data
            case 'breed':
                breed = dom_element.firstChild.data
            case 'bark':
                bark = dom_element.firstChild.data
    
    new_dog = Dog( name , breed , bark )
    new_dog.sayHi()
    
    return( new_dog )


def createXMLCat( attr: list ) -> Dog:
    
    for dom_element in attr:
        
        match dom_element.tagName:
            
            case 'name':
                name = dom_element.firstChild.data
            case 'breed':
                breed = dom_element.firstChild.data
    
    new_cat = Cat( name , breed )
    new_cat.sayHi()
    
    return( new_cat )


def readXMLAnimals():
    
    file_name = "animals.xml"
    file_path = os.path.join( HERE , file_name )
    
    xmldoc = minidom.parse( file_path )
    
    animals = xmldoc.getElementsByTagName('Animals')[0]
    
    for animal in animals.childNodes:
        
        if type( animal ) != minidom.Element:
            continue
        
        species = animal.tagName
        attr = [ x for x in animal.childNodes if type( x ) == minidom.Element ]
        print( 'Reading animal: ' + species )
        match species:
            
            case 'Dog':
                createXMLDog( attr )
            
            case 'Cat':
                createXMLCat( attr )
            
            case 'Capybara':
                print( 'Capybaraaaaa ♫ Capybaraaaa ♫ Capybara Capybara Capybara' )
                
            case 'Pollito':
                print( 'Er pollito dice pío. Cuando tiene hambre, cuando tiene frío' )
            
            case _:
                print( 'Unkown action for species: ' + species )
        
        
        print('')


# Launching the equivalent of a main() function in C++
if __name__ == '__main__':
    
    option = 1
       
    while option != '0':
        print( 'Pick a case to display:' )
        print( '( 1 ) Write class as XML' )
        print( '( 2 ) Read XML and make class' )
        print( '( 0 ) exit' )
        print( '-----' )
        
        option = input( 'Pick a choice: ' )
        
        match option:
            case '1':
                writeXMLAnimals()
            case '2':
                readXMLAnimals()
            case '0':
                print( 'Exiting....' )
            case _:
                print( option, '= Invalid option' )
        
        _ = input( 'Press enter to continue.' )
        print( '-'*50 )
        print( '\n' )