# Given an array, rotate the array by one position in clock-wise direction
def rotate( arr, n):
    a=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=a 
    return arr 
      
N = 5
A =[1, 2, 3, 4, 5]
print(rotate(A,N))    