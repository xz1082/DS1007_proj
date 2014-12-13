import unittest
import pandas as pd
from user_input_process import *
from prediction_model import *
from FinalProject import *

class test_age_validation(unittest.TestCase):
    
    def test_ageRange(self):
        self.assertFalse(age_validation('10'))
    
    def test_ageSpace(self):
        self.assertTrue(age_validation(' 20 '))
    
    def test_ageAlphabet(self):
        self.assertFalse(age_validation('abc'))
    
    def test_ageTrue(self):
        self.assertTrue(age_validation('30'))

class test_education_validation(unittest.TestCase):
    
    def test_educationIncorrectName(self):
        self.assertFalse(education_validation('college'))
    
    def test_educationNumbers(self):
        self.assertFalse(education_validation('123'))
    
    def test_educationSpace(self):
        self.assertTrue(education_validation(' Doctorate '))
    
    def test_educationTrue(self):
        self.assertTrue(education_validation('Associate'))

class test_marital_validation(unittest.TestCase):
    
    def test_maritalIncorrectName(self):
        self.assertFalse(marital_validation('single'))
    
    def test_maritalNumbers(self):
        self.assertFalse(marital_validation('123Married'))
    
    def test_maritalSpace(self):
        self.assertTrue(marital_validation(' Never-married '))
    
    def test_maritalTrue(self):
        self.assertTrue(marital_validation('Divorced'))
        
class test_ocupation_validation(unittest.TestCase):
    
    def test_ocupationIncorrectName(self):
        self.assertFalse(ocupation_validation('manager'))      
    
    def test_ocupationNumbers(self):
        self.assertFalse(ocupation_validation('123Sales'))
    
    def test_ocupationSpace(self):
        self.assertTrue(ocupation_validation('  Sales   '))
    
    def test_ocupation_True(self):
        self.assertTrue(ocupation_validation('Prof-specialty'))
        self.assertTrue(ocupation_validation('Farming-fishing'))
    
class test_capital_gain_validation(unittest.TestCase):
    
    def test_capital_gain_Range(self):
        self.assertFalse(capital_gain_validation('-1'))
        self.assertFalse(capital_gain_validation('200000000'))
        
    def test_capital_gain_space(self):
        self.assertTrue(capital_gain_validation('     1000   '))
    
    def test_capital_gain_alphabet(self):
        self.assertFalse(capital_gain_validation('fdsfds'))
    
    def test_capital_gain_true(self):
        self.assertTrue(capital_gain_validation('1200'))
    
class test_hours_per_week_validation(unittest.TestCase):
    
    def test_hours_per_week_Range(self):
        self.assertFalse(hours_per_week_validation('-10'))
        self.assertFalse(hours_per_week_validation('200'))
    
    def test_hours_per_week_space(self):
        self.assertTrue(hours_per_week_validation('     50   '))

    def test_hours_per_week_alphabet(self):
        self.assertFalse(hours_per_week_validation('fdsfds'))
    
    def test_hours_per_week_true(self):
        self.assertTrue(hours_per_week_validation('30'))
    
class test_parsefunc(unittest.TestCase):
    
    def setUp(self):
        self.parse_object = parse_func()
    
    def test_parseAge(self):
        self.assertEqual(self.parse_object.parse_age('30'), 30)
    
    def test_parseEducation(self):
        self.assertEqual(self.parse_object.parse_education('Doctorate'), 1)
        self.assertEqual(self.parse_object.parse_education('Below 12th'), 6)
    
    def test_parseMaritalStatus(self):
        self.assertEqual(self.parse_object.parse_marital_status('Married-spouse-absent'), 2)
        self.assertEqual(self.parse_object.parse_marital_status('Never-married'), 3)
    
    def test_parseOcupation(self):
        self.assertEqual(self.parse_object.parse_ocupation('Adm-clerical'), 0)
        self.assertEqual(self.parse_object.parse_ocupation('Other-service'), 7)
    
    def test_parseCapitalGain(self):
        self.assertEqual(self.parse_object.parse_capital_gain('10000'), 10000)
        
    def test_parseHoursPerWeek(self):
        self.assertEqual(self.parse_object.parse_hours_per_week('40'), 40)
        
    def tearTown(self):
        self.parse_object = None

class test_randomForest(unittest.TestCase):
    
    def testRandomForest(self):
        self.assertEqual(randomForest(pd.Series([21, 2, 3, 12, 1000, 40])), 0)
    
    def testRandomForestFalse(self):
        self.assertNotEqual(randomForest(pd.Series([21, 2, 3, 12, 1000, 40])), 10)

class test_secure_input(unittest.TestCase):
    
    def testSecureInput(self):
        #enter 20 for your age when testing
        self.assertEqual(secure_input(age_validation, 'please enter your age: ', parse_func.parse_age), 20)
    
    def testSecureInputFalse(self):
        #enter 10 for your age when testing
        self.assertNotEqual(secure_input(age_validation, 'please enter your age: ', parse_func.parse_age), 10 )

if __name__ == '__main__':
    unittest.main()
    
    