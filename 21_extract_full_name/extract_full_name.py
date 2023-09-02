def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']


    """
    full_names = [f"{person['first']} {person['last']}" for person in people]  #person for person in people...
    return full_names
   # namelist = []
   # 
   # for first in people.values():
   #     namelist.append(first)
   #     return namelist
#
    people = [
            {'first': 'Ada', 'last': 'Lovelace'},
            {'first': 'Grace', 'last': 'Hopper'},
         ]
    #namelist = names[0]['first'] + names[0]['last'] 
 