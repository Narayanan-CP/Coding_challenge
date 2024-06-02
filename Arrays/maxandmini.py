def getMinMax( a, n):
    largest=a[0]
    
    for x in a:
        if x>largest:
            largest=x
     
   
    smallest=a[0]
    for y in a:
        if y<smallest:
            smallest=y
    return (smallest,largest)
n= 6
a = [3, 2, 1, 56, 10000, 167]
print(getMinMax(a,n))
       
    