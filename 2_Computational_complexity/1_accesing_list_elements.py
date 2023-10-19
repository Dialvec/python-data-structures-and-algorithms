"""
To test the behavior of Python lists we can write a program that randomly stores
and retrieves values in a list. We can test two different theories in this program.

1. The size of a list does not affect the average access time in the list.
2. The average access time at any location within a list is the same, regardless of its location within the list.
"""

import datetime
import random
import time
import os

from statistics import mean

HERE = os.path.dirname(__file__)


def writeListAccessTimingXML( x_list , y_list ):
    file_name = "ListAccessTiming.xml"
    file_path = os.path.join( HERE , file_name )
    
    # Write an XML file with the results
    file = open( file_path , "w" )
    
    file.write( '<?xml version="1.0" encoding="UTF-8" ?>\n' )
    file.write( '<Plot title="Average List Element Access Time">\n' )
    file.write( '\t<Axes>\n' )
    file.write( '\t\t<XAxis min="' + str( min( x_list ) ) + '" max="' + str( max( x_list ) ) + '">List Size</XAxis>\n' )
    file.write( '\t\t<YAxis min="' + str( min( y_list ) ) + '" max="' + str( max( y_list ) ) + '">Microseconds</YAxis>\n' )
    file.write( '\t</Axes>\n' )
    file.write( '\t<Sequence title="Average Access Time vs List Size" color="red">\n' )
    
    for i in range( len( x_list ) ):
        file.write('\t\t<DataPoint x="' + str( x_list[ i ] ) + '" y="' + str( y_list[ i ] ) + '"/>\n' )
    
    file.write( '\t</Sequence>\n' )
    file.write( '</Plot>\n' )
    file.close()


def printListAccessTiming( x_list , y_list ):
    
    print( 'List Size vs Average Access Time' )
    
    for i in range( len( x_list ) ):
        print('List size = ' + str( x_list[ i ] ) + ' - Access time = ' + str( y_list[ i ] ) + ' us' )
    
    print('')
    print( 'Average List Element Access Time Summary:' )
    print( 'List size: min = '   + str( min( x_list ) ) + '; max = ' + str( max( x_list ) ) )
    print( 'Access time: min = ' + str( min( y_list ) ) + '; max = ' + str( max( y_list ) ) + '; mean = ' + str( mean( y_list ) ) + ' microseconds' )
    print('')
    

def listAccessTiming():
    
    # Test lists of size 1000 to 200000.
    x_min = 1000
    x_max = 200000
    
    total_retrievals = 1000
    
    # Record the list sizes in xList and the average access time in yList for 1000 retrievals
    x_list = []
    y_list = []
    
    for list_size in range( x_min , x_max + 1 , 1000 ):
        
        # Create a list of size list_size with a random value between 0 and 100
        my_list = [ random.randint( 0 , 100 ) ] * list_size
        
        # Start timer before the 1000 test retrievals
        start_time = datetime.datetime.now()
        
        # Find a random location within the list and retrieve a value.
        # Do a dummy operation with that value to ensure it is really retrieved.
        for retrieval in range( total_retrievals ):
            index = random.randint( 0 , list_size - 1 )
            retrieved_value = my_list[ index ]
            dummy = index * retrieved_value

        # End timer before the 1000 test retrievals
        end_time = datetime.datetime.now()
        
        elapsed_time = end_time - start_time

        # Compute average retrieval time in microseconds
        average_time = elapsed_time/total_retrievals
        average_time = elapsed_time.microseconds
        
        x_list.append( list_size )
        y_list.append( average_time )
    
    writeListAccessTimingXML( x_list , y_list )
    printListAccessTiming( x_list , y_list )
    

# Launching the equivalent of a main() function in C++
if __name__ == '__main__':
    
    option = 1
       
    while option != '0':
        print( 'Pick a case to display:' )
        print( '( 1 ) List access timing' )
        print( '( 2 ) ' )
        print( '( 0 ) exit' )
        print( '-----' )
        
        option = input( 'Pick a choice: ' )
        
        match option:
            case '1':
                listAccessTiming()
            case '2':
                pass
            case '0':
                print( 'Exiting....' )
            case _:
                print( option, '= Invalid option' )
        
        _ = input( 'Press enter to continue.' )
        print( '-'*50 )
        print( '\n' )