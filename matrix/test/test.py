"""
Bobby Palmer, CSC 240, Project 2
Test: This testing suite is formatted as a computer science class problem set.
"""
from matrix.matrix_operations import *


def reader(filename):
    """
    Function accepts a text file as input, reads the data from the file, and generates Matrix objects which are
    stored in a list that is returned by the function.
    :param filename: A string path to a text file in the project directory.
    :return: A list of Matrix objects, generated from the date file.
    """
    class1= []
    dataFile = open(filename, 'r')

    for line in dataFile:
        x1, x2 = line.split()
        class1.append(Matrix(2, 1, [float(x1), float(x2)]))

    dataFile.close()
    return class1

def problem2():
    """
    Simple function to display problem 2 readout. 
    """
    aData = [0, 0, 0, 0, 5.6, 1, 0, 0, 0, -47.5, 0, 1, 0, 0, -90.55, 0, 0, 1, 0, 55.25, 0, 0, 0, 1, 2.6]
    a = Matrix(5, 5, aData)
    print(leverrier(a))

    domEigenValue = powerMethod(a)

    print()
    print("The dominant eigenvalue is: ")
    print(domEigenValue)


if __name__ == "__main__":
    class1 = reader("testdata.txt")
    mean = meanFinder(class1)
    covar = covariance(class1, mean)
    covarTrace = trace(covar)
    covarDeterminant = determinant(covar)

    print("The class mean is:")
    print(mean)
    print("The covariance matrix is:")
    print(covar)
    print("The trace of the covariance matrix is:")
    print(covarTrace)
    print("\n" + "The determinant of the covariance matrix is:")
    print(covarDeterminant)

    # print("x1 \t x2")
    # for matrix in class1:
    #     print(matrix.matrix[0][0], "\t", matrix.matrix[1][0])

    print("\nThe covariance eigenvalues are:")
    eigenvalue1, eigenvalue2 = findEigenvalue(covar)
    print(eigenvalue1,",", eigenvalue2)

    eigenvector1 = add(findEigenvector(covar, eigenvalue1), mean)
    eigenvector2 = add(findEigenvector(covar, eigenvalue2), mean)

    print("\nThe unit eigenvector from the first eigenvalue is: \n" + str(eigenvector1))
    print("The unit eigenvector from the second eigenvalue is: \n" + str(eigenvector2))

    print("")
    problem2()

    amatrix = Matrix(3, 3, [1,2,3,0,4,-1,0,5,1])
    print(determinant(amatrix))


