""" 
A recursive function is simply a function that calls itself.
The recursive call must have a base case (one wait out of the recursion), 
otherwise it would keep pushing activation records on the run-time stack until we fill it up, creating a stack overflow error.

The base case in a recursive function must be written first, before the function is called recursively.
"""

""" 
When writing recursive functions we want to think more about what it does than how itworks.

When writing a recursive function there are four rules that you adhere to. 

These rules are not negotiable and will ensure that your recursive function will eventually finish:

1. Define:
    - The function name
    - The arguments that must be passed to it to complete its work
    - What value the function should return.
    
2. Write the base case for your recursive function. 
    The base case is an if statement that handles a very simple case in the recursive function by returning a value.
    
3. Call the function recursively with an argument or arguments that are smaller in some way than the parameters 
    that were passed to the function when the last call was made. 
    The argument or arguments that get smaller are the same argument or arguments you examined in your base case.
    
4. Pick some values to try out with your recursive function. 
    Trust that the recursive call you made in the last step works.
    Take the result from that recursive call and use it to form the result you want your function to return.
    Use the concrete example to help you see how to form that result.
"""

# Remember from Computational complexity: This method is NOT the most efficient for adding the n numbers.
# However, we display it for educational purposes
def recSumFirstN( n: int ) -> int:
    """Recursively adds the first n numbers.

    Args:
        n: An integer of the maximum number to add, starting from 0.

    Returns:
        Summation of first n numbers.
    """
    
    # Base case
    if n == 0:
        return 0
    # No else statement is required as there are only two choices: base case or recursion
    # Recursive call with smaller value
    return n + recSumFirstN( n-1 )
    
""" 
Note that for the case n = 4 the algorithm would go as follows:

recSumFirstN( n = 4 ):
    return 4 + recSumFirstN( n = 3 ):
        return 3 + recSumFirstN( n = 2 ):
            return 2 + recSumFirstN( n = 1 ):
                return 1 + recSumFirstN( n = 0 ):
                    return 0

Once all the activation records ran, we can see that all those nested returns end up being 4 + ( 3 + ( 2 + ( 1 + ( 0 ) ) ) ) 
Breaking up the parenthesis we get finally 4 + 3 + 2 + 1 + 0

That is how recursion works
"""


def recFactorial( n: int ) -> int:
    """Recursively computes the factorial of a number.

    Args:
        n: An integer to compute the factorial from.

    Returns:
        Factorial of n.
    """
    
    if n == 0:
        return 1
    
    return n*recFactorial( n-1 )


def recReverseString( x: str ) -> str:
    """Recursively reverses a string.

    Args:
        x: A string to be reversed.

    Returns:
        Reversed string.
    """
    
    if len( x ) == 0:
        return ""
    
    return recReverseString( x[ 1: ] ) + x[ 0 ]



def is_sorted( list1 ):
    """Checks if a list is sorted recursively.

    Args:
        list1: A list to be checked.

    Returns:
        True if the list is sorted, False otherwise.
    """

    if len( list1 ) <= 1:
        return True
    
    return list1[0] <= list1[1] and is_sorted(list1[1:])


def fibonacci(n):
    """Calculates the Fibonacci sequence recursively.

    Args:
        n: A non-negative integer.

    Returns:
        The nth Fibonacci number.
    """

    if n == 0 or n == 1:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)


def gcd(a, b):
    """Finds the greatest common divisor of two numbers recursively.

    Args:
        a: A number.
        b: Another number.

    Returns:
        The greatest common divisor of a and b.
    """

    if b == 0:
        return a
    
    return gcd(b, a % b)



# Launching the equivalent of a main() function in C++
if __name__ == '__main__':
    
    option = 1
       
    while option != '0':
        print( 'Pick a case to display recursion:' )
        print( '( 1 ) Add up first n numbers' )
        print( '( 2 ) Factorial of a number' )
        print( '( 3 ) Reverse a string' )
        print( '( 4 ) Get the n_th fibonacci number' )
        print( '( 0 ) exit' )
        print( '-----' )
        
        option = input( 'Pick a choice: ' )
        
        match option:
            case '1':
                x = input( 'Input a number' )
                x = int( x )
                recSumFirstN( x )
            case '2':
                x = input( 'Input a number' )
                x = int( x )
                recFactorial( x )
            case '3':
                x = input( 'Input a string' )
                recReverseString( x )
            case '4':
                x = input( 'Input a number' )
                x = int( x )
                fibonacci( x )
            case '0':
                print( 'Exiting....' )
            case _:
                print( option, '= Invalid option' )
        
        _ = input( 'Press enter to continue.' )
        print( '-'*50 )
        print( '\n' )