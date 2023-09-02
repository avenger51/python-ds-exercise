def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

##
##I guess loop over and check for False?
##l.copy() to return a copy?

    #set2 = set(l2)

    #return [val for val in l1 if val in set2]??

#for element in lst:
#        if lst.index(element) == True:
#            return element
#       

    return [val for val in lst if val]   #really..


# NOTE THAT A COMPREHENSION IS A FALSY CHECK.....
