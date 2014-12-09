import pandas as pd
import numpy as np

#read data into pandas dataframe with column names
df = pd.read_csv('adult_data.txt')
df.columns = ['age','workclass','fnlwgt','education','education-num','martial-status','ocupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','y']

#print df
#drop fnlwgt because we do not need to weight the observations in this project, drop education_num because it's perfectly correlated with education
df = df.drop(['fnlwgt', 'education-num'], 1)
df = df[pd.notnull(df['y'])]
df = df.drop_duplicates()

#convert target variable y to binary variable: 1 for > 50k, 0 for <= 50k
from sklearn import preprocessing 
le_y = preprocessing.LabelEncoder()
df.y = le_y.fit_transform(df.y)

#drop values '?' in workclass column 
df['workclass'] = df['workclass'].replace(' ?', np.nan)
df = df[pd.notnull(df['workclass'])]
#combine government employed into one group, self-employed into one group, never-worked and without-pay into one group, and convert them to numerical values
workclass_map = {' Never-worked': 4, ' Without-pay': 4, ' Local-gov': 1, ' State-gov': 1, ' Federal-gov': 1, ' Private': 2, ' Self-emp-not-inc': 3, ' Self-emp-inc': 3}
df['workclass'] = df.workclass.map(workclass_map)

#combine below college education into one group, associate degress into one group, and convert to numerical values
education_map = {' Doctorate': 1, ' Masters': 2, ' Bachelors': 3, ' Assoc-acdm': 4, ' Assoc-voc':4, ' Some-college': 4, ' Prof-school': 5, ' 10th': 6, ' 11th': 6, ' 12th': 6, ' 1st-4th': 6, ' 5th-6th': 6, ' 7th-8th': 6, ' 9th': 6, ' Preschool': 6, ' HS-grad': 6}
df['education'] = df.education.map(education_map)

#combine married into one category, no spouse at the time into one category, and convert to categorical values
martial_map = {' Married-AF-spouse': 1, ' Married-civ-spouse': 1, ' Married-spouse-absent': 2, ' Separated': 2, ' Divorced': 2, ' Never-married': 3, ' Widowed': 4}
df['martial-status'] = df['martial-status'].map(martial_map)

#drop missing values in ocupation column
df['ocupation'] = df['ocupation'].replace(' ?', np.nan)
df = df[pd.notnull(df['ocupation'])]
#assign categorical values to each ocupation, each race, and each gender 
for variable in ['ocupation', 'race', 'sex']:
    new = 'le_' + variable
    new = preprocessing.LabelEncoder()
    df[variable] = new.fit_transform(df[variable])

#combine husband and wife into one category, not in family currently into one category, own child is one category, and convert to category values
relationship_map = {' Husband': 1, ' Wife': 1, ' Own-child': 2, ' Not-in-family': 3, ' Other-relative': 3, ' Unmarried': 3}
df['relationship'] = df['relationship'].map(relationship_map)

#drop missing values in native-country column
df['native-country'] = df['native-country'].replace(' ?', np.nan)
df = df[pd.notnull(df['native-country'])]
#group countries by income per capita rank by International Monetary Fund, and convert to categorical values
country_map = {' United-States': 1, ' Hong': 1, ' Holand-netherlands': 1, ' Ireland': 1, ' Germany': 1, ' Canada': 1, ' Taiwan': 2, ' France': 2, ' Japan': 2, ' England': 2, ' Italy': 2, ' South': 2, ' Portugal': 3, ' Greece': 3, ' Poland': 3, ' Hungary': 3, ' Mexico': 4, ' Iran': 4, ' Thailand': 4, ' Cambodia': 5, ' China': 5, ' Columbia': 5, ' Cuba': 5, ' Dominican-Republic': 5, ' Ecuador': 5, ' El-Salvador': 5, 'Guatemala': 5, ' Haiti': 5, ' Honduras': 5, ' India': 5, ' Jamaica': 5, ' Laos': 5, ' Nicaragua': 5, ' Outlying-US(Guam-USVI-etc)': 5, ' Peru': 5, ' Philippines': 5, ' Puerto-Rico': 5, ' Scotland': 5, ' Trinadad&Tobago': 5, ' Vietnam': 5, ' Yugoslavia': 5}
df['native-country'] = df['native-country'].map(country_map)

