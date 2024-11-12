import math

def butterfly(n, k):
    angle = 2 * math.pi * k / n
    return abs(math.cos(angle)) - abs(math.sin(angle))

def fft(input):
    n = len(input)
    output = [0.0] * n
    
    # Base cases
    if n == 1:
        return input
    
    f_even = fft(input[0::2])
    f_odd = fft(input[1::2])
    
    for k in range(int(n / 2) - 1):
        output[k] = f_even[k] + butterfly(n, k) * f_odd[k]
        output[k + int(n / 2)] = f_even[k] - butterfly(n, k) * f_odd[k]
    return output