list=input("Enter list:").split()
i=len(list)-1
counter = 0
def maxElem(list,i):
    """
    This fuempty_listnction is counting how many elements equal max element in list
    Args:
        list: list
        i: integer number
    Returns:
        number of elements which equal max element in list
    Raises:
        ValueError
    Examples:
        >>>print(maxElem([1, 1, 1, 1, 2, 3], 0))
        1
        
        >>>print(func([1, 1, s, 2, 2, 3], 0))
        Traceback (most recent call last):
            ...
        ValueError
    """
    global counter
    if list[i]==max(list):
        counter+=1
    if i==0:
        return counter
    if i != 0:
        return maxElem(list,i-1)
print(maxElem(list,i))

input()
