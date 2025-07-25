# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import warnings
warnings.filterwarnings('ignore')

# load dataset
# Replace 'your_path_here.csv' with the correct path to your dataset
movie_data=pd.read_csv('your_path_here')

# split input and output
input_data=movie_data.drop(columns=['Interest'])
output_data=movie_data['Interest']

# train-test split
train_input_data,test_input_data,train_output_data,test_output_data=train_test_split(input_data,output_data,test_size=0.2,random_state=42)

# train decision tree
movie_model=DecisionTreeClassifier()
movie_model.fit(train_input_data,train_output_data)

# accuracy=accuracy_score(movie_interest,test_output_data)
# print('The Accuracy Score is : ',accuracy)

def predict_interest():
  try:
    age=int(input('Enter the Age :'))
    gender_=input('Enter the Gender(Male/Female) :').strip().lower()

    if gender_ not in ['male','female']:
      print("Invalid, Enter either Male or Female")
      return

    gender=1 if gender_=='male' else 0

    movie_interest=movie_model.predict([[age,gender]])

    print(f"\nMovie Interest for a {age} year old {gender_} : {movie_interest[0]}")

  except ValueError:
    print("invalid Input")

predict_interest()
