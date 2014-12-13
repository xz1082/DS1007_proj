from data_clean import *
from sklearn.ensemble import RandomForestClassifier


def randomForest(pred_data):
    '''
    this function takes a panda serie of input data, builds a Random Forest model on our census data, and outputs the target value calculated via the Random Forest model
    the Random Forest model excludes native-country, sex, race, workclass, capital-loss, and relationship because they do not have significant feature importance    
    '''
    model_data = clean_data_for_prediction('adult_data.txt')
    rf = RandomForestClassifier(n_estimators=150, min_samples_split=1)
    rf.fit(model_data.drop(['y', 'native-country', 'sex', 'race', 'workclass', 'capital-loss', 'relationship'], axis =1), model_data['y']) 
    income = rf.predict(pred_data)
    return income

