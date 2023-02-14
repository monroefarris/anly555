import random

def findMedian(n):
    values = [random.uniform(0, 100) for i in range(n)]
    return findKthSmallest(values, (n-1)//2)

def findKthSmallest(values, k):
    if len(values) == 1:
        return values[0]

    pivot = values[0]
    left = [x for x in values[1:] if x <= pivot]
    right = [x for x in values[1:] if x > pivot]

    if k < len(left):
        return findKthSmallest(left, k)
    elif k == len(left):
        return pivot
    else:
        return findKthSmallest(right, k-len(left)-1)
