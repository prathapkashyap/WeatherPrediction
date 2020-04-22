import requests
import pandas as pd
import json
from pandas.io.json import json_normalize

# response=requests.get("http://api.openweathermap.org/data/2.5/onecall?lat=30.489772&lon=-99.771335&lang=zh_cn")
apiKey="f4d79744fef7500fbb77a6bcbd5e49e8"
response=requests.get("http://api.worldweatheronline.com/premium/v1/weather.ashx?key=8014ab803b504020a2b120259201004 &q=bengaluru&format=json&num_of_days=1")

# print(response.json()["data"]["current_condition"][0])
# print(response.json()["data"]["weather"])

# mintempC         3176 non-null int64  weather
# DewPointC        3176 non-null int64  weather[0][hourly][0]["DewPointC"]
# FeelsLikeC       3176 non-null int64  weatherDesc
# HeatIndexC       3176 non-null int64  weatherDesc 
# WindChillC       3176 non-null int64  weatherDesc
# WindGustKmph     3176 non-null int64   same
# cloudcover       3176 non-null int64    same 
# precipMM         3176 non-null float64  same
# pressure         3176 non-null int64    same
# tempC            3176 non-null int64    take temp_C in current condition
# visibility       3176 non-null int64   current_condition
# winddirDegree    3176 non-null int64   current_condition
# windspeedKmph    3176 non-null int64   current_condition
# print(response.json()["data"]["weather"][0]["mintempC"])
# print(response.json())

# mintempC         3176 non-null int64
# DewPointC        3176 non-null int64
# FeelsLikeC       3176 non-null int64
# HeatIndexC       3176 non-null int64
# WindChillC       3176 non-null int64
# WindGustKmph     3176 non-null int64
# cloudcover       3176 non-null int64
# precipMM         3176 non-null float64
# pressure         3176 non-null int64
# tempC            3176 non-null int64
# visibility       3176 non-null int64
# winddirDegree    3176 non-null int64
# windspeedKmph    3176 non-null int64


todayConditions={}
todayConditions["mintempC"]=response.json()["data"]["weather"][0]["mintempC"]
todayConditions["DewPointC"]=response.json()["data"]["weather"][0]["hourly"][0]["DewPointC"]
todayConditions["FeelsLikeC"]=response.json()["data"]["current_condition"][0]["FeelsLikeC"]

todayConditions["HeatIndexC"]=response.json()["data"]["weather"][0]["hourly"][0]["HeatIndexC"]
todayConditions["WindChillC"]=response.json()["data"]["weather"][0]["hourly"][0]["WindChillC"]
todayConditions["WindGustKmph"]=response.json()["data"]["weather"][0]["hourly"][0]["WindGustKmph"]
todayConditions["cloudcover"]=response.json()["data"]["current_condition"][0]["cloudcover"]
todayConditions["precipMM"]=response.json()["data"]["current_condition"][0]["precipMM"]
todayConditions["pressure"]=response.json()["data"]["current_condition"][0]["pressure"]

todayConditions["tempC"]=response.json()["data"]["current_condition"][0]["temp_C"]
todayConditions["visibility"]=response.json()["data"]["current_condition"][0]["visibility"]
todayConditions["winddirDegree"]=response.json()["data"]["current_condition"][0]["winddirDegree"]
todayConditions["windspeedKmph"]=response.json()["data"]["current_condition"][0]["windspeedKmph"]

todaConditionsDf=pd.DataFrame(todayConditions,index=[0])
print(todaConditionsDf)