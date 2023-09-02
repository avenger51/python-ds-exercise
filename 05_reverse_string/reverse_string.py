def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    placeholder = ""

    for char in phrase:
        placeholder = char + placeholder

    return placeholder
    