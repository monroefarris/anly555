def allCharsPerm(listOfChars):
    '''
    recursive function that generates all unique 
    permutations of the chars in listOfChars
    '''

    if len(listOfChars) == 1:                                       # if the length of the list is 1, return a list containing that one character
        return [listOfChars[0]]
    
    # recursive case 
    else:
        permutations = []                                                  # initialize an empty list to store permutation outputs 
        for i in range(len(listOfChars)):                       
            charsLeft = listOfChars[:i] + listOfChars[i+1:]    # remove the current character
            permsLeft = allCharsPerm(charsLeft)           # generate all the permutations for the remaining characters 
            for perm in permsLeft:                             # looping through all the permutations 
                permutations.append(listOfChars[i] + perm)                 # append the current character to the beginning of the list 
        permutations = list(set(permutations))                                    # removing any duplicates 
        permutations.sort()                                                # sorting values 
        return permutations


# testing 
print(allCharsPerm(['a', 'b', 'c', 'd']))

'''
Worst case time complexity:
- T(n) = n * T(n-1)

Average case time complexity:
- Depends on list input
- Worse case can serve as an upper bound and best case can serve as a lower bound  

Best case time complexity:
- T(1) = 1x

Solving the time complexity:
    T(n) = n * T(n-1)
    = n * (n-1) * T(n-2)
    = n * (n-1) * (n-2) * T(n-3)
    = ...
    = n!

Big-O notation for complexity solution:
- O(n!)
'''