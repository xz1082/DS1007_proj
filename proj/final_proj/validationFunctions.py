# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 02:45:16 2014

@author: meinazhou

This file contains validation functions for each input of the features.
"""

def age_validation(age_input):
    '''This function validate the input of age. The function raises exceptions when th input is invalid.
    We assume the age range is [18,70]''' 
    try:
        age_input =int(age_input)
    except:
        raise invalid_age_exception
        
    if (age_input < 18) or (age_input>70):
        raise out_of_range_age_exception
    else:
        return True
    
        
        
        
class invalid_age_exception(Exception):
    '''Raise exception when the input of age is not a valid integer.'''
    def __str__(self):
        return 'The input of age is not a valid integer.' 

class out_of_range_age_exception(Exception):
    '''Raise exception when the input of age is out of the range [18,70].'''
    def __str__(self):
        return 'The input of age is out of the range.'
    