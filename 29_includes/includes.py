def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
   # """
   # #for char in collection:
   # if sought in collection:
   #     return True
   # return False

#actual answer..

    if isinstance(collection, dict):  #isinstance asking if collection = dict
        return sought in collection.values()  #if instance is a dict, then return IF? sought is in the values...?

    if start is None or isinstance(collection, set):  #isinstance asking if collection = set
        return sought in collection  #return True? if sought is in the set collection

    return sought in collection[start:] #return True? if sought is in collection using start val:0:0 slice..
