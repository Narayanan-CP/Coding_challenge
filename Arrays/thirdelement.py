def thirdLargest(a, n):
       
        firstlar=a[0]
        secondlar=-99
        thirdlar=-99
        for i in a:
            if i>firstlar:
                firstlar=i
        for y in a:
            if y>secondlar and y<firstlar:
                secondlar=y
        for z in a:
            if z>thirdlar  and z<secondlar :
                thirdlar=z
        return thirdlar 
a=[2,4,1,3,5]
n=5 
print(thirdLargest(a,n))    