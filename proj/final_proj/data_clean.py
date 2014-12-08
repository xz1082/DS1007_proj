# -*- coding: utf-8 -*-
"""Programming for DS
   Final Project
   Data_clean
   File Description: This file is imported for data cleaning process
                     particularly for the specified adult.txt data file
                     downloaded from UCI repository.                      
"""



__all__= ['data_clean']



import pandas as pd

def data_clean(uncleaned_data_path):    
    head=['age','workclass','fnlwgt','education','education-num','martial-status','ocupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','y']
    uncleaned_data=pd.read_csv(uncleaned_data_path,header=None,names=head)
    
    uncleaned_data=uncleaned_data.replace(' <=50K',0)
    uncleaned_data=uncleaned_data.replace(' >50K',1)
    uncleaned_data=uncleaned_data[pd.notnull(uncleaned_data['y'])]

    cleaned_data=uncleaned_data.drop('education-num',1)
    
    return cleaned_data
    
    
    