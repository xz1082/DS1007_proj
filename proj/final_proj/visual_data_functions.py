# -*- coding: utf-8 -*-
"""Data Visualization 
"""

__all__=['feature_category','input_validation','plot_function','add_subcategory_for_plot']

import re
import sys
from exception_files import *
import matplotlib.pyplot as plt

class feature_category:
      global cat_col,num_col
      cat_col=['workclass','education','ocupation','relationship','sex','native-country','y']
      num_col=['age','capital-gain','capital-loss']

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
             raise EmptyError('Not enough information!')
       
       
      def __repr__(self):
        return lfbrack+str(self.f)+','+self.c+rtbrack
        
        
      def data_display(self):
          print "\nFirst 10 rows in selected features: "
          print visual_data[self.f[0]][:10]
          print visual_data[self.f[1]][:10]
          print "\nUnique Values for selected Category: "
          print visual_data[self.c].value_counts()
              
      def data_summary(self):
          feature_summary=[visual_data[elem].describe() for elem in self.f] 
          category_summary=visual_data[self.c].describe()                 
          print feature_summary,category_summary 
              
          
        
def input_validation(input_be_evaluated):
    valid_fea=['age','education','ocupation','capital-gain','capital-loss','native-country']
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
        
        
def plot_function(fea_cat,sub_category):
    data_cat=visual_data[visual_data[fea_cat.c]==sub_category]
    for elem in fea_cat.f:
        data_fea=data_cat[elem]
        if elem in num_col:
           f1=plt.figure()
           ax1=f1.add_subplot(111)
           ax1.hist(data_fea.values)  
           plt.xlabel(elem)
           plt.ylabel(elem+' frequency')
           plt.title('histogram for '+elem+'with'+sub_category)  
           f1.savefig('histogram_'+elem+'with'+sub_category)
        elif elem in cat_col:
            ind=range(len(set(data_fea)))
            f2=plt.figure()
            ax2=f2.add_subplot(111)
            ax2.bar(ind,data_fea.value_counts())
            plt.xlabel(elem)
            plt.ylabel(elem+' frequency')
            plt.xticks(ind,data_fea.value_counts().index,rotation=90)
            plt.title('bar plot for '+elem+'with'+sub_category)
            f2.savefig('bar_plot_'+elem+'with'+sub_category)
                       
            
def add_subcategory_for_plot(fea_cat):
    
    while True:
       if fea_cat.c=='y':
          try:
             sub_cat=raw_input("Choose from >50K or <=50K (Upper Case): ")
             sub_cat="".join(sub_cat.split()) #remove whitespaces from user input
             if sub_cat=='quit':
                 sys.exit()
             else:
                 assert (sub_cat in ['>50K','<=50K'])
                 plot_function(fea_cat,sub_cat)
                 break
          except AssertionError:
              print 'Not valid subcategory!'
          except KeyboardInterrupt:
              sys.exit()
       elif fea_cat.c=='sex':
            try:
                sub_cat=raw_input('Choose from Female or Male(F,M Upper Case): ')
                sub_cat="".join(sub_cat.split())
                assert (sub_cat in ['Female','Male'])
                plot_function(fea_cat,sub_cat)
                break
            except AssertionError:
                print "Not valid subcategory"

