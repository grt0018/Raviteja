from statistics import mean
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("lineardataset.csv")
x=np.array(df['MARKS1'])
y=np.array(df['MARKS2'])
#print(x)
p=q=r=ypd=s=0

for i in range(len(x)):
    p=p+x[i]-mean(x)
    q=q+y[i]-mean(y)
    s=s+(y[i]-mean(y)**2)
    r=r+(x[i]-mean(x)**2)
    
m=(p*q)/r
print("slope: ",m)
c=mean(y)-m*mean(x)
print("intercept: ",c)

yp=[]
for i in range(len(x)):
    yp.append(m*x[i]+c)
    ypd=ypd+(yp[i]-mean(y)**2)
    
r_square=ypd/s
print("r square value: ",r_square)
plt.scatter(x,y,c='black')
plt.plot(x,yp,linewidth=2,marker='^',markerfacecolor='blue')
from math import sqrt
x=[2,7]
y=[9,4]
d=0

for i,j in zip(x,y):
    d=d+abs(i-j)**2
    
print("euclidean distance: ",sqrt(d))
x=[9,6]
y=[3,4]
d=0
for i,j in zip(x,y):
    d=d+abs(i-j)
    
print("manhattan distance is: ",d)
