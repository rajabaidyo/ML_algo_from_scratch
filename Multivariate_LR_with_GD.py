import pandas as pd
import numpy as np
data = pd.read_csv('hour.csv')
print(data.iloc[:5,2:17])

#setting 16 parametric coefficients as 0 and the bias as 0
#learning rate 
lr=0.00001
c=0
slope=[]
dm = []
dc =0
for i in range(14):
    slope.append(0)
    dm.append(0)
rows = data.shape[0]
# rows= int(rows/5)
cols = data.shape[1]
print('Enter the number of epochs =')
#try atleast 20 epoch
epochs = input()
sum_diff=0
for each in range(int(epochs)):
    error=0
    sum_diff=0
    for i in range(rows):
        y_actual = data.iloc[i][16]
        y_pred=0
        #print(y_actual)
        for j in range(2,cols-1):
            #print(data.iloc[i][j])
            y_pred += (data.iloc[i][j]*slope[j-2])
        y_pred+=c
        #print('y_pred=',y_pred)
        diff = y_pred - y_actual
        sum_diff+=diff
        error += diff * diff
        for j in range(2,cols-1):
            dm[j-2]+=diff*data.iloc[i][j]
    
    dc = (sum_diff)/rows
    #updating the slopes and the offset
    for j in range(14):
        slope[j]-=(lr * (dm[j]/rows))
        # print(slope[j],end =' ')
        dm[j]=0
    c -= (lr * dc)
    print('offset=',c,end=' ')
    print('error =',error/rows)