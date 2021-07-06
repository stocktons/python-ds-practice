def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # line 13 could potentially be a problem if you encounter a falsee key
    counter = {}
    for char in phrase:
        if counter.get(char): # 'if char in counter' is better
            counter[char] += 1
        else:
            counter[char] = 1

    return counter