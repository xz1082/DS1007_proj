# -*- coding: utf-8 -*-
"""Programming for DS 
   Final Project
"""


"""feature can be chose from ['age','capital-loss','capital-gain','hours-per-week','workclass','education','martial-status','ocupation','relationship','native-country','race']
   category can be chose from ['y','sex']
"""

from final_proj import *
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
      try:
        user_input=raw_input('Please enter 2 features and 1 category: ')
        user_input="".join(user_input.split()) #remove whitespaces
        if user_input=='quit':
           print "program stopped"
           sys.exit()
        else:
           try:
             fea_cat=feature_category(user_input)
             if input_validation(fea_cat):
                break
           except (NotValidForm,EmptyError,NotValidFeature,NotValidCategory,AssertionError) as e:
                print e
      except KeyboardInterrupt:
        sys.exit()
        
    print "\n-------------DATA DISPLAY------------------"  
    fea_cat.data_display()
    print "\n--------------DATA STATS SUMMARY------------"
    fea_cat.data_summary()  
    print "\n---------------DATA VISUALIZATION------------"          
    add_subcategory_for_plot(fea_cat)
          

    
    
    

if __name__== "__main__" :
     main()
     
      

       
       
           
