import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# L1.Classification
house_votes_columns = ['party', 'infants', 'water', 'budget', 'physician', 'salvador', 'religious', 'satellite', 'aid', 'missile', 'immigration', 'synfuels', 'education', 'superfund', 'crime', 'duty_free_exports', 'eaa_rsa']
house_votes = pd.read_csv('data/house-votes-84.csv', true_values=['y'], false_values=['n'], na_values=['?'], names=house_votes_columns)
house_votes.fillna(False, inplace=True)
house_votes.iloc[:,1:] = house_votes.iloc[:,1:].astype('int8')

# L3.Model Validation
nba_y_test = np.array([53, 51, 51, 49, 43, 42, 42, 41, 41, 37, 36, 31, 29, 28, 20, 67, 61, 55, 51, 51, 47, 43, 41, 40, 34, 33, 32, 31, 26, 24])
nba_predictions = np.array([60, 62, 42, 42, 30, 50, 52, 42, 44, 35, 30, 30, 35, 40, 15, 72, 58, 60, 40, 42, 45, 46, 40, 35, 25, 40, 20, 34, 25, 24])
nba_labels = np.array(['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E','E', 'E', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'])

tic_tac_toe = pd.read_csv('data/tic-tac-toe.csv')
X = pd.get_dummies(tic_tac_toe.drop('Class',axis=1))
y = tic_tac_toe['Class'].astype('category').cat.codes
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.1, random_state=42)
classifier = RandomForestClassifier(n_estimators=500, random_state=42)
classifier.fit(X_train, y_train)

diabetes = pd.read_csv('data/diabetes.csv')