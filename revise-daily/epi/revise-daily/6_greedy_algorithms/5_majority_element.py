def majority_element(arr):
    majority_element = None
    count = 0
    for n in arr:
        if count == 0:
            majority_element = n
            count = 1
        elif majority_element == n:
            count += 1
        else:
            count -= 1