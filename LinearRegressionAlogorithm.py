import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('lineardataset.csv')

#Giving input to perform LinearRegression relationship between MARKS1 and MARKS2
#x=np.array([df['MARKS1']])
#y=np.array([df['MARKS2']])

x=df['MARKS1'].values
y=df['MARKS2'].values


#Calculating mean_x and mean_y
xbar=np.mean(x)
ybar=np.mean(y)

#Calculating slope of regression line
size=len(x)
num=0
den=0
for i in range(size):
    num+=(x[i]-xbar)*(y[i]-ybar)
    den+=(x[i]-xbar)**2
    slop=num/den                  #formula for LinearRegression Slope
inter=ybar-(slop*xbar)            #ybar=slop*xbar+inter ==>  inter=ybar-(slop*xbar)
print("Slope is: ",slop)

#Finding y_pred values by using ==> y_pred=(slop*x)+inter
y_pred=[]
for i in range(size):
    res=(slop*x[i])+inter
    y_pred.append(res)

#Plotting all the values in the graph
plt.scatter(x,y,color='red')
plt.plot(x,y_pred,color='blue')
plt.show()

#Finding fitness of our regression line by using 'r2' method
# i.e finding distance between actual 'y' values and 'y_pred' values as follows
y_pred_dif=0
y_dif=0
for i in range(size):
    y_pred_dif+=(y_pred[i]-ybar)**2
    y_dif+=(y[i]-ybar)**2
fitness=y_pred_dif/y_dif
print("Mean squared error is: ",fitness)


'''
from sklearn.linear_model import LinearRegression
x=np.array([df['MARKS1']]).reshape(-1,1)
y=np.array([df['MARKS2']]).reshape(-1,1)
model=LinearRegression()
model.fit(x,y)
result=model.score(x,y)
print("Score:",result)

Score and MeanSquare error are same
'''
