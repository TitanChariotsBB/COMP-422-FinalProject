import math

# Computes the magnitude of the DFT
# That is, the sum of the absolute values of the real and imaginary parts
def dft(input):
    n = len(input)
    output = [0.0] * n
    
    # for each frequency bucket
    for k in range(n):
        sum_r = 0.0
        sum_i = 0.0
        # compute the amount of that frequency 
        # by multiplying signal by cosine at that freq
        for t in range(n):
            angle = 2 * math.pi * t * k / n
            sum_r += input[t] * math.cos(angle)
            sum_i += input[t] * math.sin(angle)
        output[k] = abs(sum_r) + abs(sum_i)
    
    return output