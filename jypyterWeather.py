{
 "nbformat": 4,
 "nbformat_minor": 2,
 "metadata": {
  "language_info": {
   "name": "python",
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   }
  },
  "orig_nbformat": 2,
  "file_extension": ".py",
  "mimetype": "text/x-python",
  "name": "python",
  "npconvert_exporter": "python",
  "pygments_lexer": "ipython3",
  "version": 3
 },
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": "hello world\n"
    }
   ],
   "source": [
    "print(\"hello world\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "import json\n",
    "from pandas.io.json import json_normalize\n",
    "\n",
    "# response=requests.get(\"http://api.openweathermap.org/data/2.5/onecall?lat=30.489772&lon=-99.771335&lang=zh_cn\")\n",
    "apiKey=\"f4d79744fef7500fbb77a6bcbd5e49e8\"\n",
    "#response=requests.get(\"http://api.worldweatheronline.com/premium/v1/weather.ashx?key=8014ab803b504020a2b120259201004 &q=bengaluru&format=json&num_of_days=1\")\n",
    "\n",
    "#print(response.json())\n",
    "with open(\"data.json\") as f:\n",
    "    jsonData=json.load(f)\n",
    "jsonString = json.dumps(jsonData, separators=(',', ':'))\n",
    "#print(jsonString)\n",
    "# print(type(jsonString))\n",
    "data = json.loads(jsonString)\n",
    "# print(data)\n",
    "jsonDataFrame=json_normalize(data['data'])\n",
    "print(jsonDataFrame.head())\n"
   ]
  }
 ]
}