class Matrix:
    """Represent a matrix in a multidimensional space."""

    def __init__(self, rows, columns, elements):
        
        # instantiating variables 
        self.rows = rows
        self.columns = columns
        self.elements = elements

    def __add__(self, other):
        """Return the matrix addition result of two matrices"""

        # throwing an exception if addition is undefined 
        if self.rows != other.rows or self.columns != other.columns:
            raise Exception("Undefined matrix addition - size mismatch")

        # creating an empty list to store results
        add_result = []

        # looping through each row in the matrix
        for i in range(self.rows):

            # checking to see if input is a matrix or a vector 
            if self.columns != 1:

                # creating an empty list to store row-wise results
                row = []

                # looping through every column in the matrix 
                for j in range(self.columns):

                    # performing the matrix addition 
                    row.append(self.elements[i][j] + other.elements[i][j])

                # appending row-wise results to final list 
                add_result.append(row)

            else:

                # appending row-wise results to final list 
                add_result.append(self.elements[i] + other.elements[i])

        # returning the matrix addition results in matrix form 
        return Matrix(self.rows, other.columns, add_result)


    def __mul__(self, other):
        """Return the matrix multiplication result of two matrices"""
        
        # throwing an exception if multiplication is undefined 
        if self.columns != other.rows:
            raise Exception("Undefined matrix multiplication - size mismatch")
        
        # creating an empty list to store results
        mult_result = []

        # looping through each row in the first matrix
        for i in range(self.rows):

            # creating an empty list to store row-wise results
            row = []

            # looping through every column in the second matrix 
            for j in range(other.columns):

                # initializing the sum counter
                sum = 0

                # looping through every row in the second matrix
                for k in range(other.rows):
                    
                    # incrementing the sum counter by the multiplication of the two matrices 
                    sum += self.elements[i][k] * other.elements[k][j]

                # adding the summed result to the list of row-wise results
                row.append(sum)

            # appending the row-wise results to the final results list 
            mult_result.append(row)

        # returning the matrix multiplication results in matrix form 
        return Matrix(self.rows, other.columns, mult_result)


class Vector(Matrix):
    """Represent a vector in a multidimensional space."""

    def __init__(self, elements):

        # instantiating variables 
        self.rows = len(elements)
        self.columns = 1
        self.elements = elements

    def outer_product(self, other):
        """Return the outer product result of two vectors"""

        # throwing an exception if outer product is undefined 
        if (self.columns != 1) or (other.columns != 1):
            raise Exception("Undefined vector outer product - size mismatch")

        # creating an empty list to store results
        outer_result = []

        # looping through all the rows of the first vector
        for i in range(self.rows):

            # creating an empty list for row-wise calculations
            row = []

            # looping through the rows of the second vector 
            for j in range(other.rows):

                # appending the product of the two row values 
                row.append(self.elements[i] * other.elements[j])

            # appending results to the final list 
            outer_result.append(row)

        # returning the outer product in matrix form 
        return Matrix(self.rows, other.rows, outer_result)


if __name__ == '__main__':

    # creating two matrices for testing 
    m_1 = Matrix(2, 2, [[1, 2], [3, 4]])
    m_2 = Matrix(2, 2, [[5, 6], [7, 8]])

    # testing the addition function from the Matrix class 
    add_test_mat = m_1 + m_2
    print(add_test_mat.elements)

    # testing the multiplication function from the Matrix class 
    mult_test_mat = m_1 * m_2
    print(mult_test_mat.elements)

    # creating two vectors for testing
    v_1 = Vector([1, 2, 3])
    v_2 = Vector([4, 5, 6])

    # testing the addition function from the Matrix class on vectors 
    add_test_vec = v_1 + v_2
    print(add_test_vec.elements)

    # testing the multiplication function from the Matrix class on vectors 
    # this throws an error (which it should!)

    # mult_test_vec = v_1 * v_2
    # print(mult_test_vec.elements)

    # testing the outer product function from the Vector class 
    outer_test_vec = v_1.outer_product(v_2)
    print(outer_test_vec.elements)

    


