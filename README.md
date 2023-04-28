# Introduction
This project focuses on the implementation of numerical algorithms for solving systems of equations in the form of: $$\Large Ax=b$$
The primary objective is to provide a code-base for users to practice and develop their understanding of the fundamentals of numerical multi-linear algebra, an essential field in mathematics and engineering. The program utilizes prebuilt commands to simplify the process while still presenting a challenge to users to create simple solutions to complex problems. With further development time, the software has the potential to solve more intricate equations. This project invites enthusiasts to contribute or improve the code, especially with the user-interface side of the project.

The are 3 main stages in total:
1. Assigning values to matrix $A$ and vector $b$
2. Selecting one of the available algorithms, which are:
    1. [Singular Value Decomposition](https://en.wikipedia.org/wiki/Singular_value_decomposition)
    2. [QR Decomposition](https://en.wikipedia.org/wiki/QR_decomposition)
    3. [LU Decomposition](https://en.wikipedia.org/wiki/LU_decomposition)
3. Outputting the results

This program is written in `Python 3`, and requires 3 libraries to be installed beforehand:
<p align="center">
    <a href="https://numpy.org/" target="_blank">
        <img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" alt="Numpy Badge" />
    </a>
    &nbsp;
    &nbsp;
    <a href="https://pandas.pydata.org/" target="_blank">
        <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas Badge" />
    </a>
    &nbsp;
    &nbsp;
    <a href="https://scipy.org/" target="_blank">
        <img src="https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white" alt="SciPy Badge" />
    </a>
</p>

---

# How to Run
For installing the required libraries, either run this command in the terminal:
```
pip install -r requirements.txt
```

Or checking out the [requirements file](https://github.com/KouroshKSH/NMLA-Algorithms/blob/master/requirements.txt) and manually install each package.

---

# How it Works
First, the program will show a quick tutorial by printing a simple message. Then, two different matrices will be shown. The user will have the option to select one of two representations, one uses the `DataFrame` data structure from Pandas library, and the other uses the `matrix` object from Numpy. The code for this section can be seen as below:
```python
def showTut():
    # show the representations via a quick tutorial
    print("\nWelcome! This program can solve a system of equations using three different methods: \n\t1) SVD\t2) QR\t3) LU")
    time.sleep(0.8)
    print("\nFirst, let's select a proper representation for the matrices.\n\tHere are the different representations:\n")
    time.sleep(0.8)

    # showing the representations with an example matrix
    example_matrix = [['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i']]
    print("\n1)\n", DataFrame(example_matrix), sep = '')
    time.sleep(0.8)
    print("\n2)\n", np.matrix(example_matrix), sep = '')
```

After that, the program will ask the user to determine the dimensions of matrix A by setting the number of rows and columns. If there are any invalid inputs, a message will be shown to notify the user that their inputs were invalid, and that they need to reenter those values. Furthermore, the user wants to redefine the dimensions of the matrix if needed.
```python
while True:
    # starting with the dimensions for matrix A
    row_A = input("\nNumber of rows for matrix A: ")
    time.sleep(0.25)
    col_A = input("\nNumber of columns for matrix A: ")
    time.sleep(0.25)

    # check if the dimensions are valid or not
    if row_A.isdigit() and col_A.isdigit():
        # store the int version of the dimensions if they're legit numbers
        row_A = int(row_A)
        col_A = int(col_A)

        decide_dimension = input(f"\nTo continue with matrix A{row_A}*{col_A}, enter 'y' for yes or 'n' to reassign the dimensions: ")
        if decide_dimension in choice_yes:
            print(f"\nThe dimensions for matrix A are stored as {row_A} and {col_A}.")
            time.sleep(0.25)
            break
        elif decide_dimension in choice_no:
            # receive the dimensions again
            continue
        else:
            print("\nYou entered an unknown input, it'll be counted as a 'no'.")
    else:
        # forces the user to give new inputs
        print("\nThe dimensions are invalid, try again.")
        time.sleep(0.25)
```

Thereafter, the program will ask the user to assign values to the elements of the matrix for each aij , where $0 \leq i < | \text{row} (A)|$ and $0 \leq j < | \text{column} (A)|$ . In each step, the terminal will print the current state of the matrix $A$ to further help the user. Naturally, the user can only enter integer or floating point numbers, otherwise, a message will be shown to notify the user to reenter the value of that element.
```python
    print("\nGiven the matrix above, we're now going to assign the elements one by one.")
    time.sleep(0.25)
    for r in range(row_A):
        for c in range(col_A):
            while True:
                # to make sure all inputs are valid
                time.sleep(0.25)
                element_input = input(f"\nValue of a[{r}][{c}]: ")

                if element_input.isdigit():
                    # to check if it's an int
                    break
                elif isFloatTry(element_input):
                    # to check if it's a float
                    break
                else:
                    print("\nInput is invalid, try again.")

            # store the floating version of inputs in matrix A
            matrix_A[r][c] = float(element_input)
            printMatrix(matrix_A, user_choice, 'A')
```

The same process will take place for vector b as well. Although, this vector will be shown as a $B_{n \times 1}$ matrix, since it will make the calculations smoother.
```python
    print("\nNow, let's define vector b.")
    while True:
        time.sleep(0.25)
        size_b = input("\nNumber of elements for vector b: ")
        if size_b.isdigit():
            size_b = int(size_b)
            time.sleep(0.25)
```

After this step, the user will see a message, which asks him to choose a method for solving the system. Entering a number from $\{ 1, 2, 3 \}$ will start the process for calling its respected algorithm. However, the user can quit the program at this stage, if needed.
```python
    print("\nNow, we can solve the system of equations with one of these methods:\n\t1) SVD\t2) QR\t3) LU")
    while True:
        time.sleep(0.25)
        decide_method = input("\nEnter the number corresponding to each method, or quit by entering '0': ")
        if decide_method in choice1:
            funcAlgSVD(matrix_A, vector_b, user_choice)
            continue
        elif decide_method in choice2:
            funcAlgQR(matrix_A, vector_b, user_choice)
        elif decide_method in choice3:
            funcAlgLU(matrix_A, vector_b, user_choice)
        elif decide_method in choice4:
            break
        else:
            print("\nNo valid input, try again.")
            continue
```

It should be noted that, all three of the algorithms use in-built commands from the libraries mentioned earlier; hence the small size of the code.
1. `funcAlgSVD(matrix_A, vector_b, user_choice)`
2. `funcAlgQR(A, b, user_choice)`
3. `funcAlgLU(A, b, user_choice)`

---

## Algorithms
### SVD
The SVD (Singular Value Decomposition) algorithm is a matrix factorization method that decomposes a matrix into three separate matrices:
1. $U$
2. $\Sigma$
3. $V$

Given an $A_{m \times n}$ matrix, we can represent it as a product of three matrices: $$A = U \Sigma V^T$$

> where $U_{m \times m}$ is an orthogonal matrix, $\Sigma_{m \times n}$ is a diagonal matrix with non-negative real numbers on the diagonal, and $V^{T}_{n \times n}$ is an orthogonal matrix.

The SVD algorithm can be used for various applications, including image compression, data analysis, and recommendation systems. It is also used in various machine learning techniques such as principal component analysis (PCA) and latent semantic analysis (LSA).
Here, three parameters are passed into this function, which are:
1. Matrix $A$, which represents the input matrix
2. Vector $b$, which is used for finding the solutions
3. The user’s choice of representation

Since $A = U \Sigma V^T$, the program first calculates these three matrices by using the `np.linalg.svd()` command. It should be noted that the parameter `full_matrices` should be set to `True`. Also, the matrix $\Sigma$, which is equal to $[[ \Sigma_1, 0], [0, 0]]$, should be constructed separately.
```python
def funcAlgSVD(matrix_A, vector_b, user_choice):
    # store the choice for representation
    choice = user_choice

    # perform the SVD decomposition method by determining the 3 matrices:
    # 1)matrix U, 2)Sigma one (Sigma = [[Sigma_one, 0], [0, 0]]), 3)V transpose
    matrix_U, matrix_Sigma_one, matrix_V_trans = np.linalg.svd(matrix_A, full_matrices = True)

    # build the main Sigma matrix from Sigma_one
    matrix_Sigma = np.zeros((len(matrix_A), len(matrix_A[0])))
    for i in range(min(len(matrix_A), len(matrix_A[0]))):
        matrix_Sigma[i][i] = matrix_Sigma_one[i]
```

---

### QR
QR decomposition (also known as QR factorization) is a matrix factorization technique that decomposes a matrix into the product of an orthogonal matrix and an upper triangular matrix. It is widely used in numerical linear algebra and has many applications in various fields, such as signal processing, optimization, and statistics. Given a matrix $A_{m \times n}$ with linearly independent columns, QR decomposition expresses $A$ as the product of an $m \times n$ orthogonal matrix $Q$ and an $n \times n$ upper triangular matrix $R$:
$$A=QR$$

> where $Q$ is an orthogonal matrix, meaning that its columns are orthonormal (i.e., unit vectors that are orthogonal to each other), and $R$ is an upper triangular matrix, meaning that all its entries below the diagonal are zero.
