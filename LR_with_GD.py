listx=[1,2,3,4,5,6,7]
listy=[4,5,6,7,8,9,10]
# m = slope and c = offset/bias
m=0
c=0
#learning rate 
l = 0.001
predict=[]
error=0
dm = 0
dc =0
print('Enter the number of epoch=')
epochs = input()
for i in range(int(epochs)):
    for j in range(len(listx)):
        diff = (listy[j]-(m*listx[j]+c))
        error += diff * diff
        dm += listx[j]*diff
        dc += (-1)*diff

    #updating the slope and offset
    m+=(l*dm)
    c+=(l*dc)
    if (i+1)%5==0 :
        print('epoch ',i+1)
        print('error=',error/len(listx))
        print('slope=',m,' offset=',c)
    dm=0
    dc=0
    error=0

#after training you can run the prediction code