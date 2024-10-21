import math

def fft(input):
    N : int = len(input)

    #we want to pad our matrix with zeroes because dividing our matrix will eventually require its length to be a power of 2
    mat_len : int = pow(2, math.ceil( math.log2( N ) ))

    padded_input = [0.0] * mat_len
    for i in range(N):
        padded_input[i] = input[i]

    output = [0.0] * N

    operator_matrix = construct_matrix(N, mat_len)

    for k in range(N):
        row_sum = 0.0
        for n in range(N):
            row_sum += operator_matrix[k][n] * padded_input[n]
        output[k] = row_sum

    return output


    

    


def construct_matrix(N:int, mat_len:int):
    mat = []
    
    for n in range(mat_len):
        mat.append([])
        for k in range(mat_len):
            if n < N and k < N:
                angle = 2 * math.pi * n * k / N
                mat[n].append( abs(math.sin(angle)) + abs(math.cos(angle)) )
            else: mat[n].append(0.0)

    return mat

#recursively divide the matrix until it's small enough that multiplication is almost linear
#def divide_matrix():

if(__name__ == "__main__"):
    matrix8 = construct_matrix(6)
    print(matrix8)