# Basic Matrix Operations

The following matrix operations package was developed for use in a university scientific computing class. The package was developed to provide functionality for creating matrix objects of any dimension and performing common matrix operations upon them. The culminating effort of this project was a naive Baye's classification function which allows fast and accurate classification of data sets in any dimension. Additionaly the project provides the ability to calculate eigen-values and eigen-vectors and the characteristic polynomial of high-degree polynomials.

## Getting Started
Upon cloning this repository the package labelled "matrix" may be moved to the source directory of any python project and imported via the following command "from matrix import * ".

The following is an example of creating a matrix object and performing an operation on it:

```
data1 = [1, 0, 0, 1]
data2 = [3, 2, 1, 11, 6, 9]

matrix1 = Matrix(2, 2, data1)
matrix2 = Matrix(3, 2, data2)

product = multiply(matrix2, matrix5)
print(product)
```

### Prerequisites

Python v 3.4 or higher.

## Running the tests

In the test directory execute "test.py" in the intepretor. The results will be displayed in CLI.

### Break down into end to end tests

The tests included in the test program are the project problems from the class assignment for which this project was created.


## Authors

* **Bobby Palmer** - *Sole Contributor* - [of20thmaine](https://github.com/of20thmaine)

## Acknowledgments

* Special thanks to UNCW Professor Gene Tagliarini whose excellent instruction made this project possible.
