import math

def fft(input):
    N : int = len(input)

    #we want to pad our matrix with zeroes because dividing our matrix will eventually require its length to be a power of 2
    mat_len : int = pow(2, math.ceil( math.log2( N ) ))

    padded_input = [0.0] * mat_len
    for i in range(N):
        padded_input[i] = input[i]

    operator_matrix = construct_matrix(N, mat_len)

    output = apply_mat(operator_matrix, padded_input, N)

    return output

def construct_matrix(N:int, mat_len:int):
    mat = []
    
    for n in range(mat_len):
        mat.append([])
        for k in range(mat_len):
            if n < N and k < N:
                angle = 2 * math.pi * n * k / N
                mat[n].append(angle)
            else: mat[n].append(0.0)

    return mat

def apply_mat(operator_matrix, input, N):
    output = [0.0] * N

    for k in range(N):
        real_sum = 0.0
        imag_sum = 0.0
        for n in range(N):
            real_sum += math.cos(operator_matrix[k][n]) * input[n]
            imag_sum += math.sin(operator_matrix[k][n]) * input[n]
        output[k] = abs(real_sum) + abs(imag_sum)

    return output

#recursively divide the matrix until it's small enough that multiplication is almost linear
#def divide_matri():

if(__name__ == "__main__"):
    matrix8 = construct_matrix(6)
    print(matrix8)