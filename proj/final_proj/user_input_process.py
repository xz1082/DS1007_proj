from user_exceptions import *

def age_validation(age_input):
    '''This function validates the input of age. The function raises exceptions when th input is invalid.
    We assume the age range is [18,70]''' 
    try:
        age_input =int(age_input)
        if (age_input < 18) or (age_input>70):
            raise out_of_range_age_exception
        else:
            return True
    except:
        return False
        raise invalid_age_exception
    
def education_validation(education_input):
    '''This function validates the input of education. The function raises exception when the input is invalid.'''      
    education_input = ''.join(education_input.split())
    
    if education_input in ['Doctorate', 'Masters', 'Bachelors', 'Associate', 'Prof-school', 'Below 12th']:
        return True 
    else:
        return False

def marital_validation(marital_input):
    '''This function validates the input of martial status.'''
    marital_input = ''.join(marital_input.split())
    if marital_input in ['Married', 'Married-spouse-absent', 'Separated', 'Divorced', 'Never-married', 'Widowed']:
        return True
    else:
        return False 

def ocupation_validation(ocupation_input):
    '''This function validates the input of ocupation.'''
    ocupation_input = ''.join(ocupation_input.split())
    if ocupation_input in ['Adm-clerical', 'Armed-Forces', 'Craft-repair', 'Exec-managerial', 'Farming-fishing', 'Handlers-cleaners', 'Machine-op-inspct','Other-service', 'Priv-house-serv', 'Prof-specialty', 'Protective-serv','Sales', 'Tech-support', 'Transport-moving']:
        return True
    else:
        return False
 
def capital_gain_validation(capital_gain_input):
    '''
    This function validates the input of capital gain. This function raises exception when the input of capital gain is out of range.
    We assume the range is [0,100000]    
    '''
    try:
        capital_gain_input =int(capital_gain_input)
        if (capital_gain_input < 0) or (capital_gain_input > 100000):
            raise out_of_range_capital_gain_exception
        else:
            return True
    except:
        return False
        raise invalid_capital_gain_exception

def hours_per_week_validation(hours_per_week_input):
    '''
    This function validates the input of hours per week. This function raises exception when the input of hours per week is out of range.
    We assume the range is [0,100]    
    '''
    try:
        hours_per_week_input =int(hours_per_week_input)
        if (hours_per_week_input < 0) or (hours_per_week_input > 100):
            raise out_of_range_capital_gain_exception
        else:
            return True
    except:
        return False
        raise invalid_hours_per_week_exception

    
class parse_func:  
    '''
    this class creates a string object and has different methods for parsing the string object into data to be processed in prediction model
    '''
    def __init__(self):
        '''
        initiate the parse function class 
        '''
        pass

    def parse_age(self, string):
        '''
        this function parses age string into integer
        '''
        return int(string)
    
    def parse_education(self, string):
        '''
        this function parses education string into a numerical value, representing categorical level of education
        '''
        if string == 'Doctorate':
            return 1
        elif string == 'Masters':
            return 2
        elif string == 'Bachelors':
            return 3 
        elif string == 'Associate':
            return 4
        elif string == 'Prof-school':
            return 5
        elif string == 'Below 12th':
            return 6
        else:
            raise unable_to_parse_exception()
    
    def parse_marital_status(self, string):
        '''
        this function parses marital status string into a numerical value, representing categorical level of marital status
        '''
        if string == 'Married':
            return 1
        elif string == 'Married-spouse-absent':
            return 2
        elif string == 'Never-married':
            return 3
        elif string == 'Widowed':
            return 4
        else:
            raise unable_to_parse_exception()

    def parse_ocupation(self, string):
        '''
        this function parses ocupation string into a numerical value, representing categorical level of ocupation
        '''
        if string == 'Adm-clerical':
            return 0
        elif string == 'Armed-Forces':
            return 1
        elif string == 'Craft-repair':
            return 2
        elif string == 'Exec-managerial':
            return 3
        elif string == 'Farming-fishing':
            return 4
        elif string == 'Handlers-cleaners':
            return 5
        elif string == 'Machine-op-inspct':
            return 6 
        elif string == 'Other-service':
            return 7
        elif string == 'Priv-house-serv':
            return 8
        elif string == 'Prof-specialty':
            return 9
        elif string == 'Protective-serv':
            return 10
        elif string == 'Sales':
            return 11
        elif string == 'Tech-support':
            return 12
        elif string == 'Transport-moving':
            return 13
        else: 
            raise unable_to_parse_exception()
    
    def parse_capital_gain(self, string):
        '''
        this function parses capital gain string into integer
        '''
        return int(string)

    def parse_hours_per_week(self, string):
        '''
        this function parses hours per week string into integer
        '''
        return int(string)


    
