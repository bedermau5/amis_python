def sum(x,n,i,iterator):
    """
    This function summ number in range from i to n
  
    Args:
        x:integer number
        n:integer number
        i:integer number
        iteration:integer number

    Returns:
        Summa of elements
    
    Raises:
        ZeroDivisionError,ValueError.
        
    Examples:
        >>>print(sum(5,5,0,0)
        0,312
        
        >>>print(sum(0,5,0,0)
        Traceback (most recent call last):
          ...
        ZeroDivisionError: division by zero
        
        >>>print(sum(a,5,0,0)
        Traceback (most recent call last):
          ...
        ValueError: invalid literal for int() with base 10: 'a'
    """
    
    result = 0
    if iterator == n:
      return result
    else:
      i=i+1    
      result = i/x**i
      return result+sum(x,n,i,iterator+1)
x=int(input("x:"))
n=int(input("n:"))
print(sum(x,n,0,0))

input()
