import numpy as np
import pandas as pd 
import  matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
path="C:\\Users\\User\\OneDrive\\AI module imp data file\\house_area_selling_price x^2.csv"
data=pd.read_csv(path,header=0,names=["train_data","labels"])
#drow the figure

data.plot(kind="scatter",x="train_data",y="labels",figsize=(20,10))
#print(data.describe())
data["labels"]=data["labels"].clip(lower=0)#all label data<0 now equal zero 
#print(data.describe())
data.plot(kind="scatter",x="train_data",y="labels",figsize=(20,10))
data=data[data["labels"]>=1]#all data = 0 now is deleted 
#print(data.describe())
data.plot(kind="scatter",x="train_data",y="labels",figsize=(20,10))
data.insert(0,"one's",1)
data=np.matrix(data)
det=data.shape[1]#the shape of data is (775,3)
#print(det)>> 3

X=data[:,:det-1]
y=data[:,det-1:]
X=np.hstack((X,np.power(X[:,1],2)))
x_std=np.std(X,axis=0)#>>>>[[   0.         1302.56495756]]
x_std[x_std==0]=1# or x_std[0,0]=1 >>>[[1.00000000e+00 1.30256496e+03]]
x_mean=np.mean(X,axis=0)
x_mean[0]=0
X=(X-x_mean)/x_std
y=(y-np.mean(y,axis=0))/np.std(y,axis=0)
plt.figure(figsize=(8,5))
x1=X[:,1].T
x2=X[:,2].T.A1
x1=x1.A1
y1=y.T.A1
#print(y1.shape)
#print(x1.shape)
#plot the first feuture with table
plt.scatter(x1, y1, color='blue', label='Feature 1 vs Target')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.title('Scatter Plot of Features vs Target')
plt.legend()
plt.show()
#plot secound feture with table 

plt.scatter(x2,y1,c="red",label="feture 2 vs target ")
plt.xlabel("featre")
plt.ylabel("target")
plt.title("scatter plot of feature 2 vs target ")
plt.legend()
plt.show()
print("x  shape is \n",X.shape)# (775, 2)
print(X)
print("y shape is \n",y.shape)#(775, 1)
theta=np.matrix(np.zeros((1,X.shape[1])))
print(theta,theta.shape) # [[0. 0. 0.]] (1, 3)
######
#cost function 
def cost(X,y,theta):
    initcost=np.power(X*theta.T-y,2)
    return (np.sum(initcost))/(2*len(X))
#parametar
alfa=0.01
itera=1000
###############
#gredian_descent function
def gredian_descent(X,y,theta,alfa,itera):
    newdet=X.shape[1]
    g=np.zeros(itera)
    for i in range(itera):
        theta2=theta.copy()
        firsum=(X*theta.T)-y
        for j in range(newdet):
            theta2[0,j]=theta[0,j]-((np.sum(np.multiply(firsum,X[:,j])))*(alfa/len(X)))
        theta=theta2
        g[i]=cost(X,y,theta)
    return g,theta    
g,theta=gredian_descent(X, y, theta, alfa, itera)
print("final theta is >>",theta)
#print (g)
########################
#plot iteration vs cost line 
plt.figure(figsize=(10,10))
plt.plot(range(itera),g,c="red",label="iteration vs cost ")
plt.xlabel("iteration")
plt.ylabel("cost")
plt.title("chick cost progretion")
plt.legend()
plt.show()
###
#plot a fit line >>>.
""" * or np.multiply is element-wise multiplication but x.dot() is used for matrix multiplication """

plt.figure(figsize=(8, 5))
x_fit = np.linspace(np.min(x1), np.max(x1), 200)
X_fit = np.column_stack((np.ones(x_fit.shape[0]), x_fit, x_fit**2))#very importint <<<<
#print(X_fit.shape)>(200, 3) here the X is capital not small 
y_fit = X_fit.dot(theta.T)
plt.scatter(x1, y1, color='blue', label='Data')
plt.plot(x_fit, y_fit, label='Quadratic Fit', color='red')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.title('Quadratic Fit to Data')
plt.legend()
plt.show()
##############################
"""
3d almost not impportant for now 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 1], X[:, 2], y, color='blue', label='Data')  # X[:,1] = x1, X[:,2] = x2
ax.set_xlabel('Feature x1')
ax.set_ylabel('Feature x2')
ax.set_zlabel('Target y')
plt.legend()
plt.show()
"""


      
            

