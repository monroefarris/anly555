
import random
import matplotlib.pyplot as plt

class ToyData:

    def __init__(self, size):
        '''
        Create a new set of toy data 

        size    integer value of size to add
        '''
        self._data = []         # creating data list instance
        self._size = size       # creating size integer instance

    def generate(self):
        '''
        Randomly generates _size floating point values between 0 and 1 
        and stores them into _data
        '''
        for i in range(self._size):             #running the methodology _size times
            self._data.append(random.random())  # appending a random number between 0 and 1 to _data

    def display(self):
        '''
        Plots a histogram of the values stored in the data list 
        '''
        plt.hist(self._data)        # plotting histogram of data list values
        plt.xlabel('Value')         # changing X Label 
        plt.ylabel('Frequency')     # changing Y Label
        plt.title('Distribution of Values in\n Data List')  # changing title
        plt.show()                  # showing the plot

# testing of ToyData class and subsequent methods

td = ToyData(5)             # instantiating the ToyData class 
print(td._data)             # printing the contents of _data
print(td._size)             # printing the contents of _size

td.generate()               # calling the generate method 

print(td._data)             # printing the contents of _data
print(td._size)             # printing the contents of _size

td.display()                # calling the display method 

