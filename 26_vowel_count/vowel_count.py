def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = ('a', 'e', 'i', 'o', 'u')
    vowel_counts = {char: phrase.count(char) for char in phrase if char in vowels}
    return vowel_counts
# vowels = ('a', 'e', 'i', 'o', 'u')
    #{char:0 for char in phrase if char in vowels}   #phrase if char in vowels}
    #return 
    
    #for char in phrase:
    #    if char in vowels:
    #        return char