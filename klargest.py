def Largest(arr, k): 
    arr.sort(reverse=True) 
    for i in range(k): 
        print (arr[i],end=" ")  
  
# Driver program 
arr = [1, 23, 12, 9, 30, 2, 50] 
k = 3
Largest(arr, k) 
