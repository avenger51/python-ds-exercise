def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    #for char in phrase:
    #    if char.isupper() == True:
    #        return 
    #if to_swap.isupper():
#I 100% had to check the solution for this one..

    to_swap = to_swap.lower()  #why is this turned all into lowercase??
    out = ""

    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        out += ltr

    return out