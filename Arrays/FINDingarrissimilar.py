
# Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not. 
# Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation) of elements may be different though.
# Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.
def check(A,B):
        C=len(A)
        D=len(B)
        
        # if C!=D:
        #     return 0
        A.sort()
        B.sort()
        if(A==B):
            return 1
        else:
            return 0
A = [1,2,5,4,0]
B = [2,4,5,0,1]  
print(check(A,B))      
        