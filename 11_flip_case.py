def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # lower case 
    to_swap = to_swap.lower()
    swapped_string = ''
    
    for char in phrase:
        if char.lower() == to_swap:
            swapped_string += char.swapcase()
        else:
            swapped_string += char

    return swapped_string


