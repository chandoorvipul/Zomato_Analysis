# -*- coding: utf-8 -*-
"""
Created on Mon May 27 21:35:27 2019

@author: chand
"""
import pandas as pd 
import numpy as np

data = pd.read_csv("states_all.csv")
d = data.head(10);
print(data.isnull().sum())
print(data.isnull().values.any())
print(data.isnull().sum().sum())
#median = data['AVG_READING_8_SCORE'].median()
#print(median)
#data['AVG_READING_8_SCORE'].fillna(median, inplace = True)
#print(data.isnull().sum())
DC = ['YEAR','ENROLL','TOTAL_REVENUE',
       'FEDERAL_REVENUE', 'STATE_REVENUE', 'LOCAL_REVENUE',
       'TOTAL_EXPENDITURE', 'INSTRUCTION_EXPENDITURE',
       'SUPPORT_SERVICES_EXPENDITURE', 'OTHER_EXPENDITURE',
       'CAPITAL_OUTLAY_EXPENDITURE', 'GRADES_PK_G', 'GRADES_KG_G',
       'GRADES_4_G', 'GRADES_8_G', 'GRADES_12_G', 'GRADES_1_8_G',
       'GRADES_9_12_G', 'GRADES_ALL_G', 'AVG_MATH_4_SCORE', 'AVG_MATH_8_SCORE',
       'AVG_READING_4_SCORE', 'AVG_READING_8_SCORE']
print(data[DC])
for i in DC:
    med = i
    a = data[med].median()
    print(i, a)
    print(data[med].fillna(a, inplace = True))
print(data.isnull().sum())
print(data[DC])



import matplotlib.pyplot as plt

plt.plot(data.YEAR, data.STATE_REVENUE)
plt.plot(data.YEAR, data.LOCAL_REVENUE)
plt.legend(["State revenue", "Local Revenue"])
plt.title("State vs Local Revenue")
plt.xlabel("Year")
plt.ylabel("revenue")

plt.show()

