# -*- coding: utf-8 -*-
"""Data Visualization 
"""

__all__=['feature_plot']



class category:
    def __repr__(self):
        return 
        
        
        
        
            def __repr__(self):
        return self.lrbd+str(self.lfnum)+','+str(self.rtnum)+self.upbd
        
    def __init__(self,rep):
       """define the input as an interval with 6 attributes:
       self.lfnum represents the left numerical value from the input
       self.rtnum represents the right numerical value from the input
       self.lrbd represents the left parenthesis from the input
       self.upbd represents the right parenthesis from the input 
       self.minval represents the smallest integer number in the interval
       self.maxval represents the largest integer number in the interval
       self.span represents the collection of intergers that are covered in the interval
       """
       self.rep=rep 
       self.num=self.rep[1:-1].split(",")
       self.lfnum=int(self.num[0])
       self.rtnum=int(self.num[1])
       self.lrbd=rep[0]
       self.upbd=rep[-1]
    
def feature_plot(feature,category):
    data_cat=adult_data[adult_data[category[0]]==category[1]]
    data_for_feature=data_cat[feature]
    if feature in num_col:
       data_for_feature.hist()
    elif feature in cat_col:
        data_for_feature.value_counts().plot(kind='barh')
    
    
    