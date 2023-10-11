"""
You can read text (among other types) files and do operations on the file's data.
Each line of the file will contain a record with the needed information.
"""
""" 
single_lines.txt contains line with comma-separated values.
- lines starting with 'user' denote a user we want to greet
--- Users will have a name, an email and, possibly, phone numbers (we do not know how many)
- lines starting with 'sqr' denote a number we want to compute its squared value
- No actions are defined for other line starters
"""
# Library os will help us to navigate through the file system
import os

# Path to current file's directory
here = os.path.dirname(__file__)

# Function to greet a user
def greetUser( name: str , email: str , *phone_numbers: list ):
        
        print( 'Greetigs dear' , name )
        print( 'We will contact you at' , email )
        
        if len( phone_numbers ) > 0 :
            print( 'Or call you to' , *phone_numbers )
        
# Function to print the squared number of a value
def computeSqr( x: int ):
    print( 'Squared value of', x, 'is', x*x )


def readSingleLines():
    file_name = "single_lines.txt"
    file_path = os.path.join( here , file_name )
    
    file = open( file_path , mode = "r" )
    
    for line in file:
        
        # The strip method strips off the newline character at the end of the line
        # and any blanks that might be at the beginning or end of the line.
        text = line.strip()
        
        # Separate each comma-separated value in a variable
        # Star '*' notation packs second and remaining values from the line in a list
        command, *args = text.split(',')
        
        # Here we still may have head and trailing spaces, let's get rid of them
        command = command.strip()
        args = [ x.strip() for x in args ]
        
        match command:
            case 'user':
                # Start notation for packing the phone numbers in args
                name , email , *phone_numbers = args
                greetUser( name , email , *phone_numbers )
            
            case 'sqr':
                # At this point we still have the value as string. Let's turn it into numeric
                # Remember args is a list. So we need to get the first and only element
                x = int(args[0])
                computeSqr( x )
                
            # Default case for unknown line starters. Note the underscore
            case _:
                print( 'No operation defined for command:', command )
            
        print('')

"""
What if wee need to process multiple lines as block?
You may need a second loop to read lines until certain condition is met. Like in our case is finding a semicolon ';'.
It is called the Loop and a Half Pattern.

Note that lines do not necesarily end in comma
"""

def readMultipleLines():
    file_name = "multiple_lines.txt"
    file_path = os.path.join( here , file_name )
    
    file = open( file_path , mode = "r" )
    
    command_line = ""
    
    for line in file:
        
        text = line.strip()
        # Concatenate current line's contents with previous value in command_line
        command_line = command_line + text
        
        if( ';' not in text ):
            # Add a comma in case no comma exists
            command_line = command_line + ','
            
        else:
            # Remember to remove the semicolon
            command_line = command_line.replace( ';' , '')
            
            command, *args = command_line.split(',')
            
            command = command.strip()
            args = [ x.strip() for x in args ]
            
            match command:
                case 'user':
                    name , email , *phone_numbers = args
                    greetUser( name , email , *phone_numbers )
                
                case 'sqr':
                    x = int(args[0])
                    computeSqr( x )
                    
                case _:
                    print( 'No operation defined for command:', command )
            
            command_line = "" # Clear command_line
        print('')


# Launching the equivalent of a main() function in C++
if __name__ == '__main__':
    
    option = 1
       
    while option != '0':
        print( 'Pick a case to display:' )
        print( '( 1 ) Read data from single lines' )
        print( '( 2 ) Read data across multiple lines' )
        print( '( 0 ) exit' )
        print( '-----' )
        
        option = input( 'Pick a choice: ' )
        
        match option:
            case '1':
                readSingleLines()
            case '2':
                readMultipleLines()
            case '0':
                print( 'Exiting....' )
            case _:
                print( option, '= Invalid option' )
        
        _ = input( 'Press enter to continue.' )
        print( '-'*50 )
        print( '\n' )