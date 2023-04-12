import numpy as np
import scipy.linalg as la
from pandas import DataFrame
import time


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


def printMatrix(givern_matrix, user_choice, name_of_matrix):
    givern_matrix = np.around(givern_matrix, 5)
    if user_choice == 1:
        # pandas representation
        print(f'\n{name_of_matrix} = ', DataFrame(givern_matrix), sep = '\n')
    else:
        # numpy representation
        print(f'\n{name_of_matrix} = ', np.matrix(givern_matrix), sep = '\n')


def isFloatTry(givern_input):
    # to check if a given number is float or not
    try:
        float(givern_input)
        return True
    except ValueError:
        return False


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

    # proof for the legitimacy of the algorithm
    print("\nThe main matrices of the SVD algorithm will be printed to showcase its functionality.")
    time.sleep(0.45)
    printMatrix(matrix_U, choice, 'U')
    time.sleep(0.45)
    printMatrix(matrix_Sigma, choice, 'Σ')
    time.sleep(0.45)
    printMatrix(matrix_V_trans, choice, 'V^{T}')
    time.sleep(0.45)
    print("\nSince 'A = U @ Σ @ V^{T}', we can see that:")
    matrix_prove = np.around(matrix_U @ (matrix_Sigma @ matrix_V_trans), 5)
    time.sleep(0.45)
    printMatrix(matrix_prove, choice, 'A = U @ Σ @ V^{T}')
    time.sleep(1.25)

    # calculate the pseudo inverses and transposes of the matrices
    matrix_A_inverse = np.linalg.pinv(matrix_A)
    matrix_V = np.matrix.transpose(matrix_V_trans)
    matrix_Sigma_inverse = np.linalg.pinv(matrix_Sigma)
    matrix_U_trans = np.matrix.transpose(matrix_U)

    print("\nNow, if we calculate the inverse of matrix A, or 'A^{-1}', we can see that:")
    printMatrix(matrix_A_inverse, choice, 'A^{-1}')
    time.sleep(0.45)
    printMatrix(matrix_V, choice, 'V')
    time.sleep(0.45)
    printMatrix(matrix_Sigma_inverse, choice, 'Σ^{-1}')
    time.sleep(0.45)
    printMatrix(matrix_U_trans, choice, 'U^{T}')
    print("\nSince 'A^{-1} = V @ Σ^{-1} @ U^{T}', we can see that:")
    matrix_prove = np.around(matrix_V @ (matrix_Sigma_inverse @ matrix_U_trans), 5)
    time.sleep(0.45)
    printMatrix(matrix_prove, choice, 'A^{-1} = V @ Σ^{-1} @ U^{T}')
    time.sleep(1.25)

    # show that both routes work
    print("\nAt last, we can find the values of our system of equation.")
    time.sleep(0.45)
    print("\n1) Calculating 'x' using 'Ax = b >> x = A^{-1} @ b':")
    vector_x = np.around(matrix_A_inverse @ vector_b, 5)
    time.sleep(0.45)
    printMatrix(vector_x, choice, 'A^{-1} @ b = x')
    time.sleep(0.45)
    print("\n2) Calculating 'x' using 'A = U @ Σ @ V^{T}, Ax = b >> x = V @ Σ^{-1} @ U^{T} @ b':")
    vector_x = np.around(matrix_V @ (matrix_Sigma_inverse @ (matrix_U_trans @ vector_b)), 5)
    time.sleep(0.45)
    printMatrix(vector_x, choice, 'V @ Σ^{-1} @ U^{T} @ b = x')
    time.sleep(1.25)

    print("\n\nVoila!\n")


def funcAlgQR(A, b, user_choice):
    choice = user_choice

    # perform the QR decomposition by determining matrices Q and R
    Q, R = np.linalg.qr(A)

    # proof for the legitimacy of the algorithm
    print("\nThe main matrices of the QR algorithm will be printed to showcase its functionality.")
    time.sleep(0.45)
    printMatrix(Q, choice, 'Q')
    time.sleep(0.45)
    printMatrix(R, choice, 'R')
    time.sleep(0.45)
    print("\nSince 'A = Q @ R', we can see that:")
    matrix_prove = np.around(Q @ R, 5)
    time.sleep(0.45)
    printMatrix(matrix_prove, choice, 'A = Q @ R')
    time.sleep(1.25)

    A_inv = np.linalg.pinv(A)
    R_inv = np.linalg.pinv(R)
    Q_trans = np.matrix.transpose(Q)

    print("\nNow, if we calculate the inverse of matrix A, or 'A^{-1}', we can see that:")
    printMatrix(A_inv, choice, 'A^{-1}')
    time.sleep(0.45)
    printMatrix(R_inv, choice, 'R^{-1}')
    time.sleep(0.45)
    printMatrix(Q_trans, choice, 'Q^{T}')
    time.sleep(0.45)
    print("\nSince 'A^{-1} = R^{-1} @ Q^{T}', we can see that:")
    matrix_prove = np.around(R_inv @ Q_trans, 5)
    time.sleep(0.45)
    printMatrix(matrix_prove, choice, 'A^{-1} = R^{-1} @ Q^{T}')
    time.sleep(1.25)

    print("\nAt last, we can find the values of our system of equation.")
    time.sleep(0.45)
    print("\n1) Calculating 'x' using 'Ax = b >> x = A^{-1} @ b':")
    x = np.around(A_inv @ b, 5)
    time.sleep(0.45)
    printMatrix(x, choice, 'A^{-1} @ b = x')
    time.sleep(0.45)
    print("\n2) Calculating 'x' using 'A = Q @ R, Ax = b >> x = R^{-1} @ Q^{T} @ b':")
    x = np.around(R_inv @ (Q_trans @ b), 5)
    time.sleep(0.45)
    printMatrix(x, choice, 'R^{-1} @ Q^{T} @ b = x')
    time.sleep(1.25)

    print("\n\nVoila!\n")


def funcAlgLU(A, b, user_choice):
    choice = user_choice

    # perform the LU decomposition using pivot
    P, L, U = la.lu(A)

    print("\nThe main matrices of the LU algorithm will be printed to showcase its functionality (with row pivoting).")
    time.sleep(0.45)
    printMatrix(P, choice, 'P')
    time.sleep(0.45)
    printMatrix(L, choice, 'L')
    time.sleep(0.45)
    printMatrix(U, choice, 'U')
    time.sleep(0.45)
    print("\nSince 'A = P @ L @ U', we can see that:")
    matrix_prove = np.around(P @ (L @ U), 5)
    time.sleep(0.45)
    printMatrix(matrix_prove, choice, 'A = P @ L @ U')
    time.sleep(1.25)

    A_inv = np.linalg.pinv(A)
    U_inv = np.linalg.pinv(U)
    L_inv = np.linalg.pinv(L)
    P_trans = np.matrix.transpose(P)

    print("\nNow, if we calculate the inverse of matrix A, or 'A^{-1}', we can see that:")
    printMatrix(A_inv, choice, 'A^{-1}')
    time.sleep(0.45)
    printMatrix(U_inv, choice, 'U^{-1}')
    time.sleep(0.45)
    printMatrix(L_inv, choice, 'L^{-1}')
    time.sleep(0.45)
    printMatrix(P_trans, choice, 'P^{T}')
    time.sleep(0.45)
    print("\nSince 'A^{-1} = U^{-1} @ L^{-1} @ P^{T}', we can see that:")
    matrix_prove = np.around(U_inv @ (L_inv @ P_trans), 5)
    time.sleep(0.45)
    printMatrix(matrix_prove, choice, 'A^{-1} = U^{-1} @ L^{-1} @ P^{T}')
    time.sleep(1.25)

    print("\nAt last, we can find the values of our system of equation.")
    time.sleep(0.45)
    print("\n1) Calculating 'x' using 'Ax = b >> x = A^{-1} @ b':")
    x = np.around(A_inv @ b, 5)
    time.sleep(0.45)
    printMatrix(x, choice, 'A^{-1} @ b = x')
    time.sleep(0.45)
    print("\n2) Calculating 'x' using 'A = P @ L @ U, Ax = b >> x = U^{-1} @ L^{-1} @ P^{T} @ b':")
    x = np.around(U_inv @ (L_inv @ (P_trans @ b)), 5)
    time.sleep(0.45)
    printMatrix(x, choice, 'U^{-1} @ L^{-1} @ P^{T} @ b = x')
    time.sleep(1.25)

    print("\n\nVoila!\n")


def main():
    # begin the tutorial to familiarize the user
    showTut()

    # store the different possible choices
    rep1 = ['one', '1', 'One', 'ONE']
    rep2 = ['two', '2', 'Two', 'TWO']
    choice_yes = ['Y', 'y', 'yes', 'Yes', 'YES', 'yup']
    choice_no = ['N', 'n', 'no', 'No', 'NO', 'nope']
    choice1 = ['one', '1', 'One', 'ONE']
    choice2 = ['two', '2', 'Two', 'TWO']
    choice3 = ['three', '3', 'Three', 'THREE']
    choice4 = ['zero', '0', 'o', 'O', 'Zero', 'ZERO', 'exit', 'quit']

    # deciding the representation
    while True:
        time.sleep(0.25)
        user_choice = input("\nEnter the number for your desired representation: ")
        if user_choice in rep1:
            user_choice = 1
            print("\nYour choice is stored.")
            time.sleep(0.25)
            break
        elif user_choice in rep2:
            user_choice = 2
            print("\nYour choice is stored.")
            time.sleep(0.25)
            break
        else:
            print("\nInvalid input, try again.")

    # move onto the process of receiving inputs for the system
    print("\nConsidering 'Ax = b', let's define matrix 'A' and then vector 'b'.")
    time.sleep(0.8)

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

            # reasure the user of his choice
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

    # create an emmpty matrix A filled with zeros
    matrix_A = np.zeros((row_A, col_A))

    # show the default matrix
    printMatrix(matrix_A, user_choice, 'A')

    # begin the process of assigning values to a_{ij}
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

    time.sleep(0.8)

    # begin the process of assigning values to b_{i}
    print("\nNow, let's define vector b.")
    while True:
        time.sleep(0.25)
        size_b = input("\nNumber of elements for vector b: ")
        if size_b.isdigit():
            size_b = int(size_b)
            time.sleep(0.25)

            # check if the number of elements of vector b is valid (== rows of A)
            if size_b == row_A:
                decide_size = input(f"\nTo continue with vector b{size_b}, enter 'y' for yes or 'n' to reassign the number of elements: ")
                if decide_size in choice_yes:
                    print(f"\nThe dimension for vector b is stored as {size_b}.")
                    break
                elif decide_size in choice_no:
                    continue
                else:
                    print("\nYou entered an unknown input, it'll be counted as a 'no'.")
            else:
                print("\nThe number of elements of vector b should be equal to the number of rows of matrix A.")
        else:
            print("\nThe dimension is invalid, try again.")

    # create an empty vector b filled with zeros
    vector_b = np.zeros((size_b, 1))
    printMatrix(vector_b, user_choice, 'b')

    time.sleep(0.25)

    print("\nGiven the vector above, we're now going to assign the elements one by one.")
    for s in range(size_b):
        while True:
            time.sleep(0.25)
            element_input = input(f"\nValue of b[{s}]: ")
            if element_input.isdigit():
                break
            elif isFloatTry(element_input):
                break
            else:
                print("\nInput is invalid, try again.")

        vector_b[s][0] = float(element_input)
        printMatrix(vector_b, user_choice, 'b')

    time.sleep(0.75)

    # let the user choose the method
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

    # and we're done
    print("\n\nHope you enjoyed!")


if __name__ == '__main__':
    main()
