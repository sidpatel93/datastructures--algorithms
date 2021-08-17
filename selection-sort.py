def small(arr):
    '''Function to find the smallest number from the given array'''

    small = arr[0]
    smallIndex = 0
    for i in range(1,len(arr)):
        if arr[i]< small:
            small = arr[i]
            smallIndex = i
  
    return smallIndex

print(small([8,5,6,4,7,9,1]))


def selectionSort(arr):
    '''Function to sort the array using selectionsort method'''

    newArr = []
    for i in range(len(arr)):
        smallElement = small(arr)
        newArr.append(arr.pop(smallElement))

    return newArr


print(selectionSort([5,6,8,9,7,1,2,3,5,4]))