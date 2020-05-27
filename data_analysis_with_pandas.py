# -*- coding: utf-8 -*-
"""
Created on Mon May 25 18:08:29 2020

@author: erind
"""


import pandas as pd
workbook1 = 'workbook1.xlsx'
workbook2 = 'workbook2.xlsx'

#read in file from excel
df1 = pd.read_excel(workbook1)
df2 = pd.read_excel(workbook2)
print(df1.head(5))
print(df2.head(5))


#union the two data files
frame = [df1, df2]
all_data_df = pd.concat(frame, axis = 0)
print(all_data_df)


#filter the dataframe to only get Line # = 1 
line1_df = all_data_df.loc[all_data_df["Line #"] == 1])

#grouping by operators to at the average amount of time
#assgin column name to the new column as 'Avg Amount' and sort descending base on it
#get the best operator in line 1 with the highest averge productivity
productivity_df = all_data_df.groupby("Operator")['Amount'].agg('mean').reset_index(name ='Avg Amount').sort_values("Total Amount", ascending = False)
print(productivity_df)
