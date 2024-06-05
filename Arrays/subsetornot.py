
# Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m, where both arrays may contain duplicate elements. The task is to determine
# whether array a2 is a subset of array a1. It's important to note that both 
# arrays can be sorted or unsorted. Additionally, each occurrence of a duplicate element within an array is considered as a separate 
# element of the set
def isSubset( a1, a2, n, m):
    d={}
    for i in a1:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
            
    for i in a2:
        if i not in d:
            return "No"
        elif i in d and d[i]==0:
            return "No"
        else:
            d[i]-=1
    return "Yes" 
a1= [11, 7, 1, 13, 21, 3, 7, 3]
a2 = [11, 3, 7, 1, 7]
n=5
m=6
print(isSubset(a1,a2,n,m))