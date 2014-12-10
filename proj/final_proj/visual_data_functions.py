# -*- coding: utf-8 -*-
"""Data Visualization 
"""

__all__=['feature_category','feature_plot']

import re
from exception_files import *

class feature_category:
      def __init__(self,rep):
          lfbrack,middle,rtbrack=rep[0],rep[1:-1],rep[-1]
          if middle!='':
              try:
                assert ( lfbrack=='(' )
                assert ( rtbrack==')' )
                assert ( middle[0] == '[')
                occur = 2
                indices = [x.start() for x in re.finditer(",", middle)]
                assert ( middle[indices[occur-1]-1] == ']')
                f = middle[0:indices[occur-1]]
                self.f = [f.split(',')[0][1:],f.split(',')[1][:-1]]
                self.c = middle[indices[occur-1]+1:]                  
              except: 
                  raise NotValidForm(rep)
          else:
             raise EmptyError('Not enough information')
       
       
      def __repr__(self):
        return lfbrack+str(self.f)+','+self.c+rtbrack
        
        
def input_validation(input_be_evaluated):
    valid_fea=['age','education','martial-status','ocupation','capital-gain','capital-loss','hours-per-week']
    valid_cat=['y','sex']
    #validation for feature input
    for elem in input_be_evaluated.f:
        if elem not in valid_fea:
            raise NotValidFeature(elem)
    #validation for category input
    if input_be_evaluated.c not in valid_cat:
        raise NotValidCategory(input_be_evaluated.c)
    else:
        return True

def data_display(fea_cat):
    print "First 10 rows in selected features: "
    print visual_data[fea_cat.f[0]][:10]
    print visual_data[fea_cat.f[1]][:10]
    print "Unique Values for selected Category: "
    print visual_data[fea_cat.c].value_counts()
    
def feature_plot(feature,category):
    data_cat=adult_data[adult_data[category[0]]==category[1]]
    data_for_feature=data_cat[feature]
    if feature in num_col:
       data_for_feature.hist()
    elif feature in cat_col:
        data_for_feature.value_counts().plot(kind='barh')
    
    
    