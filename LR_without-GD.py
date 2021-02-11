#B1 = sum((x(i) - mean(x)) * (y(i) - mean(y))) / sum( (x(i) - mean(x))^2 )
#B0 = mean(y) - B1 * mean(x)
listx = [2,5,4,8,9]
listy = [12,67,36,89,109]
#calculating the mean
sumx=0
sumy=0
for i in range(len(listx)):
    sumx+=listx[i]
    sumy+=listy[i]
meanx = sumx/len(listx)
meany = sumy/len(listy)
print('x-mean=',meanx)
print('y-mean=',meany)
#calculating the covariance for the correlation and the variance
covariance = 0
variance = 0
for i in range(len(listx)):
    covariance += (listx[i]-meanx)*(listy[i]-meany)
    variance += (listx[i]-meanx)*(listx[i]*meanx)
print('covariance=',covariance)
print('variance=',variance)
#calculating the parameters
b1 = covariance/variance
b0 = meany - meanx * b1
print('b1=',b1)
print('b0=',b0)
#predicting the output
x = 87
print('predicted value=',b1*x+b0)