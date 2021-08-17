# Binary search Algorithm assuming that our given array is the sorted


def binarySearch(ar, item):
    ''' Binary Search algorithm with iterative solution'''

    lowPosition = 0
    highPosition = len(ar) - 1
    
    
    while(lowPosition<=highPosition):
        mid = int((lowPosition + highPosition)/2)
        # print(mid)
        guess = ar[mid]

        if(guess == item):
          return mid
            

        if(guess < item):
            lowPosition = mid +1
          
        else:
            highPosition = mid - 1
    

    return None

print(binarySearch([1,2,5,6,7,8,9,10], 2))


