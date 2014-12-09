# -*- coding: utf-8 -*-
"""Data Visualization 
"""

__all__=['feature_category','feature_plot']

import re
from exception_files import *

class feature_category:
      def __init__(self,rep):
          lfbrack,middle,rtbrack=rep[0],rep[1:-1],rep[-1]
          try:
            assert ( lfbrack=='(' ), "left"
            assert ( rtbrack==')' ), "right"
            if len(middle)!=0:
               occur = 2
               indices = [x.start() for x in re.finditer(",", middle)]
               f = middle[0:indices[occur-1]]
               self.f = [f.split(',')[0][1:],f.split(',')[1][:-1]]
               self.c = middle[indices[occur-1]+1:]
            else:
                 raise EmptyError('No content to analysis')
          except:
            raise NotValidForm(rep)
       
       
      def __repr__(self):
        return lfbrack+str(self.f)+','+self.c+rtbrack
    

user_input=raw_input()
fea_cat=feature_category(user_input)

    
def feature_plot(feature,category):
    data_cat=adult_data[adult_data[category[0]]==category[1]]
    data_for_feature=data_cat[feature]
    if feature in num_col:
       data_for_feature.hist()
    elif feature in cat_col:
        data_for_feature.value_counts().plot(kind='barh')
    
    
    