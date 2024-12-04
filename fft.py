import math
import cmath

def fft(input: list[float]):
    input = pad_input(input)
    complexResult :list[complex] = apply_fft(input)

    RealResult = [abs(X.real) + abs(X.imag) for X in complexResult]
    return RealResult


def apply_fft(input:list[float]):
    N : int = len(input)
    if not math.log2(N) == int(math.log2(N)):
        raise ValueError("Cannot run the fft on a number of samples that is not a power of 2")

    # base case
    if N == 1:
        return input

    omega = cmath.exp(2*cmath.pi*cmath.sqrt(-1)/N)

    evenElements = input[0:N:2]
    oddElements = input[1:N:2]

    # recursive calls
    evenResults = apply_fft(evenElements)
    oddResults = apply_fft(oddElements)

    output = [0 for i in range(0,N)]

    for k in range(0, int(N/2)):
        output[k] = evenResults[k] + omega**k * oddResults[k]
        output[k + int(N/2)] = evenResults[k] - omega**k * oddResults[k]

    return output

def pad_input(input):
    new_len = math.pow(2, math.ceil(math.log2(len(input))))

    while( len(input) < new_len):
        input.append(0)

    return input

if(__name__ == "__main__"):
    test_input = [1, 2, 3]
    fft(test_input)
