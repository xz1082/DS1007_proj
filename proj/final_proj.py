# -*- coding: utf-8 -*-
"""Programming for DS 
   Final Project
"""


"""feature can be chose from ['age','capital-loss','capital-gain','hours-per-week','workclass','education','martial-status','ocupation','relationship','native-country','race']
   category can be chose from ['y','sex']
"""

from final_proj import *
import sys
#cat_col=['workclass','education','martial-status','ocupation','relationship','sex','native-country','race']
#num_col=['age','capital-gain','capital-loss','hours-per-week']
#'/Users/mengfeili/Desktop/DS1007/DS1007_proj/adult.txt'


def main():
    global visual_data
    #read data
    while True:
        try:
          f_path=raw_input('Please enter the file path: ')
          if f_path!='quit':
             visual_data=clean_data_for_visual(f_path)
             print "--------DATA INFORMATION----------"
             print "DATA SHAPE: ", visual_data.shape
             print "\nChoose features from: ", str(['age','education','martial-status','ocupation','capital-gain','capital-loss','hours-per-week'])
             print "\nChoose Category from: ", str(['y','sex'])
             break
          elif f_path=='quit':
              sys.exit()
        except (ReadFileError,Exception) as e:
            print e
        except KeyboardInterrupt:
            sys.exit()
    
    print "\n--------DATA Visualization-------"
    while True:
      is_valid_input=False
      try:
        user_input=raw_input('Please enter 2 features and 1 category: ')
        if user_input=='quit':
           print "program stopped"
           sys.exit()
        else:
           try:
             fea_cat=feature_category(user_input)
             is_valid_input=input_validation(fea_cat)
             break
           except (NotValidForm,EmptyError,NotValidFeature,NotValidCategory,AssertionError) as e:
                print e
      except KeyboardInterrupt:
        sys.exit()
        
    while is_valid_input:
          data_display(fea_cat)  
          
          break
    
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

       
       
           
