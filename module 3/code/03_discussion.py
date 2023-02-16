import random

def findMedian(n):
    '''
    returns the median of 'n' random values
    '''
    # randomly generating 'n' floating point values between 0 and 100
    values = [random.uniform(0, 100) for i in range(n)]     

    # sorting values    
    values.sort()                                           

    # if length of list is even - find the two middle values and divide to get median 
    if n % 2 == 0:

        # getting right middle value 
        right = values[n//2]

        # getting left middle value 
        left = values[n//2 -1]

        # getting the average of the two values to return as the median 
        return (left + right) /2

    # if length of list is odd - median is middle value 
    else:
        return values[n//2]
  
# testing the function 
print(findMedian(3))

print(findMedian(4))

'''
Step Count 

Best Case:
- O(n)
- This happens when the list of n values comes in completely sorted, 
and the .sort() function doesn't need to be utilized 

Worst Case:
- O(n log n)
- This happens when the list of n values come in completely unsorted, 
and the .sort() function needs to be used 


Space Count 

- O(n)
- The function only needs to store the list of values in memory 


Upper Bound

- Time complexity of O(n log n) and 
space complexity of O(n), where the time 
complexity is heavily impacted by the .sort() function 
'''