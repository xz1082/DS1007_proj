import numpy as np
import pandas as pd
from data_clean import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn import linear_model


__all__=['trainTest','data_split','randomForest','logRegression']

def trainTest(dat, pct):
    '''
    Randomly splits data into train and test
    '''
    dat_shuf = dat.reindex(np.random.permutation(dat.index))
    trn = dat_shuf[:int(np.floor(dat_shuf.shape[0]*pct))]
    tst = dat_shuf[int(np.floor(dat_shuf.shape[0]*pct)):]
    return trn, tst

def data_split(predict_data):
    train, test = trainTest(predict_data, 0.8)
    lab = 'y'
    X_train, Y_train, X_test, Y_test = train.drop(lab, axis = 1), train[lab], test.drop(lab, axis = 1), test[lab]
    return X_train, Y_train, X_test, Y_test
    
def randomForest(predict_data):
    X_train, Y_train, X_test, Y_test = data_split(predict_data)
    rf = RandomForestClassifier(n_estimators=150, min_samples_split=1)
    rf.fit(X_train, Y_train) 
    imp = pd. Series(rf.feature_importances_, index = X_test.columns)
    imp.sort()
    return rf.predict_proba(X_test)[:, 1]

def logRegression(predict_data):
    X_train, Y_train, X_test, Y_test = data_split(predict_data)
    logreg = linear_model.LogisticRegression(C=1e30)
    logreg.fit(X_train,Y_train)
    logreg_prob = logreg.predict_proba(X_test)[:, 1]

    return logreg_prob
  
    
