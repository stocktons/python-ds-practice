def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    # move outside and give all caps name as a constant
    days_of_the_week = { 
        1 : "Sunday",
        2 : "Monday",
        3 : "Tuesday",
        4 : "Thursday",
        5 : "Friday",
        6 : "Saturday",
        7 : "Sunday",
    }

    return days_of_the_week.get(day_of_week)