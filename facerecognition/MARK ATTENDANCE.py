import cv2
import os
from datetime import datetime
import pandas as pd
import csv
from datetime import date


def clear_CSV(file_name):
    file = open(file_name,"r+")
    file.truncate(16)
    file.close()
    

def TOminutes(Entry,Exit):
    IN=Entry.split(':')
    OUT=Exit.split(':')
    t1=(int)(IN[0])*60 + (int)(IN[1]) 
    t2=(int)(OUT[0])*60 + (int)(OUT[1])
    return t2-t1



df1=pd.read_csv("ENTRY.csv")
df2=pd.read_csv("EXIT.csv")
LIST=pd.read_csv("LIST.csv")

result = df1.merge(df2, indicator=True, how='outer').loc[lambda v: v['_merge']=='both']
result.drop(['_merge'],axis=1, inplace=True)

result['DURATION']=0

for i in range(result.shape[0]):
    result['DURATION'][i]=TOminutes(result['Time_ENTRY'][i],result['Time_EXIT_'][i])

#dropping student records who have a duration less than a specified threshold
result= result.drop(result[result.DURATION < 1].index)

for i in range(LIST.shape[0]):
    if result.shape[0] !=0:
        for j in range(result.shape[0]):
            if result['Name'][j] == LIST['Name'][i]:
                LIST['ATTENDANCE'][i]="PRESENT"
            else:
                LIST['ATTENDANCE'][i]="ABSENT"
    else:
        LIST['ATTENDANCE'][i]="ABSENT"

'''
print(df1)
print()
print(df2) 
print()
print(result)            
print() 
'''

t = date.today()

t=t.strftime("%m-%d-%Y")
t=t+'.csv'

print(LIST)

LIST.to_csv(t)    

clear_CSV("ENTRY.csv")
clear_CSV("EXIT.csv")



