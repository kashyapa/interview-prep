def rearrange(arr):
    
    for i in range(len(arr)):
        arr[i:i+2] = sorted(arr[i:i+2], reverse=bool(i % 2))
    
    return arr
