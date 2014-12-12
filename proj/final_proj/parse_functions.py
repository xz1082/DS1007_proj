
class parse_func:  
    '''
    this class creates a string object and has different methods for parsing the string object into data to be processed in prediction model
    '''
    def __init__(self, string):
        self.string = string

    def parse_age(self):
        return int(self.string)
    
    def parse_education(self):
        if self.string == 'Doctorate':
            return 1
        elif self.string == 'Masters':
            return 2
        elif self.string == 'Bachelors':
            return 3 
        elif self.string == 'Associate':
            return 4
        elif self.string == 'Prof-school':
            return 5
        elif self.string == 'Below 12th':
            return 6
        else:
            raise unable_to_parse_exception()
    
    def parse_marital_status(self):
        if self.string == 'Married':
            return 1
        elif self.string == 'Married-spouse-absent' or 'Separated' or 'Divorced':
            return 2
        elif self.string == 'Never married':
            return 3
        elif self.string == 'Widowed':
            return 4
        else:
            raise unable_to_parse_exception()

    def parse_ocupation(self):
        if self.string == 'Adm-clerical':
            return 0
        elif self.string == 'Armed-Forces':
            return 1
        elif self.string == 'Craft-repair':
            return 2
        elif self.string == 'Exec-managerial':
            return 3
        elif self.string == 'Farming-fishing':
            return 4
        elif self.string == 'Handlers-cleaners':
            return 5
        elif self.string == 'Machine-op-inspct':
            return 6 
        elif self.string == 'Other-service':
            return 7
        elif self.string == 'Priv-house-serv':
            return 8
        elif self.string == 'Prof-specialty':
            return 9
        elif self.string == 'Protective-serv':
            return 10
        elif self.string == 'Sales':
            return 11
        elif self.string == 'Tech-support':
            return 12
        elif self.string == 'Transport-moving':
            return 13
        else: 
            raise unable_to_parse_exception()
    
    def parse_capital_gain(self):
        return int(self.string)

    def parse_hours_per_week(self):
        return int(self.string)

class unable_to_parse_exception(Exception):
    def __str__(self):
        return 'Cannot parse string'
    pass
    