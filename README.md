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
