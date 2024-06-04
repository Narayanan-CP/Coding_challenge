# This problem is done using hashing technique
def missingNumber(array,n):
        # create a list of zeroes
    temp = [0] * (n)

    for i in range(0, n-1):
        temp[array[i] - 1] = 1

    for i in range(0, n+1):
        if(temp[i] == 0):
            ans = i + 1
            break
    return ans  

array = [1, 2, 3, 5]
n = 5

   
print(missingNumber(array, n)) 
  
    