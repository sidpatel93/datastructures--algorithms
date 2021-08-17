def quick(arr):
    '''quicksort algorithm'''

    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]  # Used list comprehension concept in python
        greater = [i for i in arr[1:] if i > pivot]
        return quick(less) + [pivot] + quick(greater)
  
print(quick([5,6,8,4,2,3,1]))