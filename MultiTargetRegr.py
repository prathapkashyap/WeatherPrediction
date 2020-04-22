import os 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
import requests
a=pd.read_csv('bangalore.csv')
a=a.drop_duplicates(keep='first')
X=a.drop(['maxtempC','mintempC','humidity',"date_time",'sunHour','moonset','moonrise','totalSnow_cm','uvIndex','uvIndex.1',"moon_illumination","sunrise","sunset","winddirDegree","windspeedKmph"],axis=1)
y=a[['maxtempC','mintempC','humidity']]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=2500, test_size=600, random_state=4)

max_depth = 30
regr_multirf = MultiOutputRegressor(RandomForestRegressor(n_estimators=100,
                                                          max_depth=max_depth,
                                                          random_state=0))
regr_multirf.fit(X_train, y_train)
response=requests.get("http://api.worldweatheronline.com/premium/v1/weather.ashx?key=8014ab803b504020a2b120259201004 &q=bengaluru&format=json&num_of_days=1")
# print(response.json())
todayConditions={}
# todayConditions["mintempC"]=response.json()["data"]["weather"][0]["mintempC"]
todayConditions["DewPointC"]=response.json()["data"]["weather"][0]["hourly"][1]["DewPointC"]
todayConditions["FeelsLikeC"]=response.json()["data"]["current_condition"][0]["FeelsLikeC"]

todayConditions["HeatIndexC"]=response.json()["data"]["weather"][0]["hourly"][1]["HeatIndexC"]
todayConditions["WindChillC"]=response.json()["data"]["weather"][0]["hourly"][1]["WindChillC"]
todayConditions["WindGustKmph"]=response.json()["data"]["weather"][0]["hourly"][1]["WindGustKmph"]
todayConditions["cloudcover"]=response.json()["data"]["current_condition"][0]["cloudcover"]
todayConditions["precipMM"]=response.json()["data"]["current_condition"][0]["precipMM"]
todayConditions["pressure"]=response.json()["data"]["current_condition"][0]["pressure"]
todayConditions["tempC"]=response.json()["data"]["current_condition"][0]["temp_C"]
todayConditions["visibility"]=response.json()["data"]["current_condition"][0]["visibility"]
todayConditionsDf=pd.DataFrame(todayConditions,index=[0])
y_multirf = regr_multirf.predict(X_test)
prediction=regr_multirf.predict(todayConditionsDf)
print(todayConditions["tempC"],response.json()["data"]["current_condition"][0]["weatherDesc"][0]["value"],prediction[0][0],prediction[0][1],prediction[0][2])