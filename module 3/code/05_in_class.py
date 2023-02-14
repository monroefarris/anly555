from time import time
import matplotlib.pyplot as plt

######## PART 1 ##########
# Creating a function to print a right triangle

def printRightTriangle(height):
    '''
    Function that prints an ascii triangle (using '*'s) of height height
    '''
    start = time()                  # starting timer
    for i in range(1, height+1):    # looping through "height" amount of times
        for j in range(i):        
            print("*", end="")      # printing * character 
        print("\n")                 # printing a new line character 
    end = time()                    # ending timer 
    return end - start              # calculating time elapsed

######## PART 2 ##########
# Derive a step count function T(h) and determine a tight-fit upperbound of T(h) using Big-O notation

'''
Step count function T(h):  

    There are two loops in the printRightTriangle methodology:
        - one that runs 'h' times 
        - one that runs 'i' times where i is between 1 and 'h + 1'

    T(h) = h * (h+1)/2

Big-O Notation:     

    T(h) = O(h^2)
'''

######## PART 3 ##########
# Creating a methodology to test the runtime of the function with various triangle heights 

heights = [3, 4, 5, 6, 7, 8, 9, 10]             # setting various triangle heights to be tested
times = []                                      # creating an empty list to store results 
for height in heights:                          # looping through each of the heights in the list 
    times.append(printRightTriangle(height))    # running the right triangle function  

plt.plot(heights, times)                        # line plot of triangle height versus time  
plt.xlabel("Height of Triangle")
plt.ylabel("Runtime in Seconds")
plt.title("Comparison of Height and Runtime")
plt.show()