def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """

    return [  
         [ele for ele in lst if fn(ele) ],
         [ele for ele in lst if not fn(ele)]
    ]
def is_string(el):
        return isinstance(el, str)  #built in to check if el is 'string class'

def is_even(num):
        return num % 2 == 0

   #
    # return [
    #     [val for val in lst if fn(val)],
    #     [val for val in lst if not fn(val)]
    # ]
