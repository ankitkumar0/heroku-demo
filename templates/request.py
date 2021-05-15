# -*- coding: utf-8 -*-
"""
Created on Sat May 15 18:10:04 2021

@author: Deepak Gupta
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2, 'test_score':9, 'interview_score':6})

print(r.json())