class invalid_age_exception(Exception):
    '''Raise exception when the input of age is not a valid integer.'''
    def __str__(self):
        return 'The input of age is not a valid integer.' 
    pass

class out_of_range_age_exception(Exception):
    '''Raise exception when the input of age is out of the range [18,70].'''
    def __str__(self):
        return 'The input of age is out of the range [18,70].'
    pass

class invalid_capital_gain_exception(Exception):
    '''Raise exception when the input of capital gain is not a valid integer.'''
    def __str__(self):
        return 'The input of capital gain is not a valid integer.'
    pass
        
class out_of_range_capital_gain_exception(Exception):
    '''Raise exception when the input of capital gain is out of the range [0,100000].'''
    def __str__(self):
        return 'The input of capital gain is out of the range [0,100000].'
    pass

class invalid_hours_per_week_exception(Exception):
    '''Raise exception when the input of hours per week is not a valid integer.'''
    def __str__(self):
        return 'The input of hours per week is not a valid integer.'
    pass
        
class out_of_range_hours_per_week_exception(Exception):
    '''Raise exception when the input of capital gain is out of the range [0,100].'''
    def __str__(self):
        return 'The input of capital gain is out of the range [0,100].'
    pass

class unable_to_parse_exception(Exception):
    '''
    Raise exception when inputs are unable to parse.
    '''
    def __str__(self):
        return 'Cannot parse string'
    pass