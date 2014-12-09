# -*- coding: utf-8 -*-
"""Programming for DS 
   Final Project
"""


"""feature can be chose from ['age','capital-loss','capital-gain','hours-per-week','workclass','education','martial-status','ocupation','relationship','native-country','race']
   category can be chose from ['y','sex']
"""

from final_proj import *


def main():
    
    #adult_data=data_clean('/Users/mengfeili/Desktop/DS1007/DS1007_proj/adult.txt')
    #cat_col=['workclass','education','martial-status','ocupation','relationship','sex','native-country','race']
    #num_col=['age','capital-gain','capital-loss','hours-per-week']
    
    user_input=raw_input('Please enter 2 features and 1 category: ')
    while len(user_input)!=0:
        try:
          fea_cat=feature_category(user_input)
        except (NotValidForm,AssertionError) as e:
            print e
    

  
    
    #visulization from user input

    
       
    
    




if __name__== "__main__" :
   main()    
   
"""   
ind=random.sample(df.index,int(math.floor(df.shape[0]*0.7)))
tr_x=df.ix[ind].drop('y',1)
tr_y=df.ix[ind].y
te_x=df.ix[df.index-ind].drop('y',1)
te_y=df.ix[df.index-ind].y


rf=RandomForestClassifier(n_estimators=100)
rf=rf.fit(tr_x, tr_y)
roc_auc_score(te_y,rf.predict_proba(te_x)[:,1])
"""