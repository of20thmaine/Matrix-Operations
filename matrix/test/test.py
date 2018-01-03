"""
Bobby Palmer, CSC 240, Project 2
Test: This testing suite is formatted as a computer science class problem set.
"""
from matrix_operations import *


def reader1(filename):
    """
    Function accepts a text file as input, reads the data from the file, and generates Matrix objects which are
    stored in two lists that are returned by the function.
    :param filename: A string path to a text file in the project directory.
    :return: Two lists of Matrix objects, generated from the date file.
    """
    class1, class2 = [], []
    dataFile = open(filename, 'r')

    for line in dataFile:
        x1, x2, y1, y2 = line.split()
        class1.append(Matrix(2, 1, [float(x1), float(x2)]))
        class2.append(Matrix(2, 1, [float(y1), float(y2)]))

    dataFile.close()
    return class1, class2


def reader2(filename):
    """
    Function accepts a text file as input, reads the data from the file, and generates Matrix objects which are
    stored in a list that is returned by the function.
    :param filename: A string path to a text file.
    :return: A list of Matrix objects, generated from the date file.
    """
    class1= []
    dataFile = open(filename, 'r')

    for line in dataFile:
        x1, x2 = line.split()
        class1.append(Matrix(2, 1, [float(x1), float(x2)]))

    dataFile.close()
    return class1


def problem1():
    """Simple function to display problem 3 readout."""
    class1, class2 = reader1("testdata1.txt")
    mean1, mean2 = meanFinder(class1), meanFinder(class2)
    covariance1, covariance2 = covariance(class1, mean1), covariance(class2, mean2)
    determinant1, determinant2 = determinant(covariance1), determinant(covariance2)
    inverse1, inverse2 = inverse(covariance1), inverse(covariance2)

    totalSize = len(class1) + len(class2)
    mean1Class1Grade = grader(mean1, mean1, inverse1, determinant1, len(class1), totalSize)
    mean2Class1Grade = grader(mean2, mean1, inverse1, determinant1, len(class1), totalSize)
    mean2Class2Grade = grader(mean2, mean2, inverse2, determinant2, len(class2), totalSize)
    mean1Class2Grade = grader(mean1, mean2, inverse2, determinant2, len(class2), totalSize)

    print("Class 1 Mean:")
    print(mean1)
    print("Class 2 Mean:")
    print(mean2)

    print("Class 1 Covariance Matrix:")
    print(covariance1)
    print("Class 2 Covariance Matrix:")
    print(covariance2)

    print("Class 1 Determinant:")
    print(determinant1)
    print()
    print("Class 2 Determinant:")
    print(determinant2)
    print()

    print("Class 1 Inverse Matrix:")
    print(inverse1)
    print("Class 2 Inverse Matrix:")
    print(inverse2)

    print("The grade for Class 1's mean in Class 1 grader is:", mean1Class1Grade)
    print("The grade for Class 2's mean in Class 1 grader is:", mean2Class1Grade)
    print("The grade for Class 2's mean in Class 2 grader is:", mean2Class2Grade)
    print("The grade for Class 1's mean in Class 2 grader is:", mean1Class2Grade)
    print()

    class1outliers = []
    class2outliers = []

    print("Table of Grades:")
    print("x1", "\t", "y1", "\t", "grade1", "\t", "grade2", "\t", "x2", "\t", "y2", "\t", "grade1", "\t", "grade2",
          "\t")
    for point in range(len(class1)):
        print(class1[point].matrix[0][0], "\t", class1[point].matrix[1][0], "\t",
              grader(class1[point], mean1, inverse1, determinant1, len(class1), totalSize),
              "\t", grader(class1[point], mean2, inverse2, determinant2, len(class2), totalSize), "\t",
              class2[point].matrix[0][0], "\t",
              class2[point].matrix[1][0], "\t",
              grader(class2[point], mean1, inverse1, determinant1, len(class1), totalSize), "\t",
              grader(class2[point], mean2, inverse2, determinant2, len(class2), totalSize))

        if grader(class1[point], mean1, inverse1, determinant1, len(class1), totalSize) < grader(class1[point], mean2,
                                                                                                 inverse2, determinant2,
                                                                                                 len(class2),
                                                                                                 totalSize):
            class1outliers.append(class1[point])
        if grader(class2[point], mean1, inverse1, determinant1, len(class1), totalSize) > grader(class2[point], mean2,
                                                                                                 inverse2, determinant2,
                                                                                                 len(class2),
                                                                                                 totalSize):
            class2outliers.append(class2[point])

    print("\n" + "Misclassified Points in Class 1:")
    for point in class1outliers:
        print(point)
    print("\n" + "Misclassified Points in Class 2:")
    for point in class2outliers:
        print(point)

    print("The boundary points for the grader function are: ")
    boundaryCalculator(mean1, inverse1, determinant1, mean2, inverse2, determinant2, len(class1), totalSize)


def problem2():
    """Simple function to display problem 2 readout. """
    augmentedMatrixA_data = [3, 1, -1, 4, 1, 1, -1, -1, 2, 1, 2, 2, 0, -1, -2, 2, 2, -3, 0, -2, 5, 4, -1, 0, 3, 1, 4, 1,
                             1, -7, 3, 2, 2, -9, 0, -1, 1, 1, 2, 3, -2, 2, 2, 9, 1, 0, -3, -2, 2, 0, 2, 4, -5, -2, -2,
                             1, -1, 1, 1, -5, 0, -2, 3, 1, 0, 1, 1, 0, 2, 1, 1, -4]
    coefficientMatrixA_data = [3, 1, -1, 4, 1, 1, -1, -1, 1, 2, 2, 0, -1, -2, 2, 2, 0, -2, 5, 4, -1, 0, 3, 1, 1, 1, -7,
                               3, 2, 2, -9, 0, 1, 1, 2, 3, -2, 2, 2, 9, 0, -3, -2, 2, 0, 2, 4, -5, -2, 1, -1, 1, 1, -5,
                               0, -2, 1, 0, 1, 1, 0, 2, 1, 1]

    matrixA = Matrix(8, 9, augmentedMatrixA_data)
    matrixACoefficient = Matrix(8, 8, coefficientMatrixA_data)

    allowed, reducedMatrixA = gaussJordan(matrixA)
    determinantMatrixA = determinant(matrixACoefficient)
    inverseA = inverse(matrixACoefficient)
    detInverseA = determinant(inverseA)
    checkInverse = multiply(matrixACoefficient, inverseA)
    conditionNum = conditionNumber(matrixACoefficient, inverseA)

    print("Matrix A solutions are: ")
    if allowed is True:
        variables = ["x", "y", "z", "w", "a", "b", "c", "d"]
        for row in range(reducedMatrixA.rows):
            print(variables[row] + " = " + str(reducedMatrixA.matrix[row][reducedMatrixA.columns-1]))
    print()
    print("The determinant of Matrix A is:", determinantMatrixA, "\n")
    print("The inverse matrix of Matrix A is: ")
    print(inverseA)
    print("The determinant of the Matrix A inverse is:", detInverseA, "\n")
    print("The product of Matrix A's determinant and Matrix A inverse's determinant is:",
          determinantMatrixA * detInverseA, "\n")
    print("The product of Matrix A and its inverse is: ")
    print(checkInverse)
    print("The condition number of Matrix A is:", conditionNum, "\n")


def problem3():
    """
    Simple function to display problem 3 readout. 
    """
    class1 = reader2("testdata2.txt")
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
    print(eigenvalue1, ",", eigenvalue2)

    eigenvector1 = add(findEigenvector(covar, eigenvalue1), mean)
    eigenvector2 = add(findEigenvector(covar, eigenvalue2), mean)

    print("\nThe unit eigenvector from the first eigenvalue is: \n" + str(eigenvector1))
    print("The unit eigenvector from the second eigenvalue is: \n" + str(eigenvector2))

    print("")


def problem4():
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


def boundaryCalculator(mean1, inverse1, determinant1, mean2, inverse2, determinant2, classSize, totalSize):
    """Calculates classifier function boundary."""
    boundaryPoints = [Matrix(2,1,[-4, x]) for x in range(-6, 5, 2)]

    for point in boundaryPoints:
        while (grader(point, mean1, inverse1, determinant1, classSize, totalSize) - grader(point, mean2, inverse2,
                determinant2, classSize, totalSize)) < -0.001:
            point.matrix[0][0] += .001

    print("x1", "\t", "y1")
    for point in boundaryPoints:
        print(point.matrix[0][0], "\t", point.matrix[1][0])


if __name__ == "__main__":
    problem1()
    problem2()
    problem3()
    problem4()
