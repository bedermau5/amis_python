def CreateList(x):
    """
    This function create list with elements
  
    Args:
        element:integer number
        x:integer number
        
    Returns:
        List with elements
        
    Raises:
        ValueError
        
    Examples:
        >>>print(CreateList(2)
        >>>Enter element: 5
        >>>Enter element: 3
        ['5', '3']
        
        >>>print(CreateList(s)
        Traceback (most recent call last):
          ...
        ValueError: invalid literal for int() with base 10: 's'
    """
    if x==0:
        return list
    else:
        element = int(input("Enter element:"))
        list.append(element)
        return CreateList(x-1)
def MinElem(min,new_list,i):
    """
    This function search min element of list
  
    Args:
        min:integer number
        new_list:list
        i:integer number

    Returns:
        Number
    
    Raises:
        ValueError
        
    Examples:
        >>>print(MinElem(0, list[0], 0))
        >>>Enter element: 5
        >>>Enter element: 3
        3
        
        >>>print(MinElem(a, list[0], 0)
        Traceback (most recent call last):
          ...
        ValueError: invalid literal for int() with base 10: 'a'
    """
    if i==len(new_list):
        return min
    if new_list[i]<min:
        min=new_list[i]
    return MinElem(min,list,i+1)
list=[]
x = int(input("Length of list:"))
list = CreateList(x)
print(MinElem(list[0],list,0))

input()
