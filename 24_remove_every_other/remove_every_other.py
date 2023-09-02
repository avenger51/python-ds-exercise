def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
#newlist = [num for num in lst if num ]
    newnum = []
    for num in lst.range(0, 5, 1):
        newnum += num
    return newnum


#    loop over lst and send every other num to a new list


