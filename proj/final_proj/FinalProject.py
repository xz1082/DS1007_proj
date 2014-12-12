# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 23:37:10 2014

@author: meinazhou
"""
import sys
def main():
    while True:
        try:
            
            age =raw_input('Please enter your age.')
            education =raw_input('Please enter your education.')
            marital_status =raw_input('Please enter your marital status.')
            ocupation =raw_input('Please enter your ocupation.')
            capital_gain =raw_input('Please enter your capital gain.')
            hours_per_week =raw_input('Please enter your working hours per week.') 
        except (KeyboardInterrupt, EOFError):
            sys.exit()
            
            
def secure_input(validation_func, input_request,parse_func):
    while True:
        try:
            string = raw_input(input_request)
        except (KeyboardInterrupt, EOFError):
            #exception class
            sys.exit()
        termination_orders = ['Exit', 'End', 'Quit']
        if string in termination_orders:
            print '-----------Terminating the program.---------'
            sys.exit()
        if validation_func(string): #if the validation function returns true
            parsed_input = parse_func(string)
        else:
            #raise exception for invalid input 
    return parsed_input 
            
            
          
            
                
    