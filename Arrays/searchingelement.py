def search(arr, N, X):
    for i in range(0,len(arr)):
        if arr[i]==X:
            return i
    else:
        return "-1"
arr=[3,4,5,6,7]
N=5
X=3
print(search(arr,N,X))
# in this we are representing the place where the number is located        
                