
## QUESTION 1
def computePi4(num_terms):

    fourth_pi = 0   # initializing counter for 1/4th pi
    denom = 1       # initializing counter for denominator 

    for i in range(num_terms):     # looping through num_terms provided 

        if i % 2 == 0:             # if num_terms is even 
            fourth_pi += 1/denom   # according to the formula, 1/denom is added to 1/4th pi
    
        else:                      # if num_terms is odd
            fourth_pi -= 1/denom   # according to the formula, 1/denom is subtracted from 1/4th pi
        
        denom += 2  # incrementing the denominator by 2, per formula provided

    return fourth_pi # returning result 

print(computePi4(10000)) # printing returned result 


## QUESTION 2
def computePi4(num_terms):
    return sum(1.0/(2*i + 1)*(-1)**i for i in range(num_terms)) # comprehension syntax means of generating pi/4 

print(computePi4(10000)) # printing returned result 

## QUESTION 3
def computePi4(num_terms):
   
    fourth_pi = 0   # initializing counter for 1/4th pi
    denom = 1       # initializing counter for denominator 

    for i in range(num_terms):     # looping through num_terms provided 

        if i % 2 == 0:             # if num_terms is even 
            fourth_pi += 1/denom   # according to the formula, 1/denom is added to 1/4th pi
    
        else:                      # if num_terms is odd
            fourth_pi -= 1/denom   # according to the formula, 1/denom is subtracted from 1/4th pi
        
        denom += 2  # incrementing the denominator by 2, per formula provided

        yield fourth_pi # yielding result 

# iterating over series of results and print output
for i in computePi4(10000):

    print(i)





