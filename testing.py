import sys
import math
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) > 1:
    try:
        sample_rate = int(sys.argv[1])
    except:
        sample_rate = 1000
else:
    sample_rate = 1000
    
if len(sys.argv) > 2:
    try:
        freq = int(sys.argv[2])
    except:
        freq = 100
else:
    freq = 100
        

# define x(t) as sine wave at the given freq
xt = np.zeros(sample_rate) # initialize buffer
t_step = 2* np.pi * freq / sample_rate # increment amount for sine
t = 0.0 # initial t

# fill the buffer with samples of the sine wave
for i in range(xt.size):
    xt[i] = np.sin(t)
    t += t_step

# Plot the first two cycles of the signal
two_cycles_index = math.ceil(2 * (sample_rate / freq))
plt.plot(xt[:two_cycles_index])
plt.title("Sample index")
plt.ylabel("Value of x(t)")
plt.show()

# Plot the absolute value (magnitude) of the fft
fxt = np.fft.fft(xt)
pos_freq_bound = math.ceil(fxt.size / 2) + 1
pos_fxt_mag = np.absolute(fxt[:pos_freq_bound])
plt.plot(pos_fxt_mag)
plt.xscale("log")
plt.title("Absolute value of the FT of x(t)")
plt.ylabel("Magnitude")
plt.xlabel("Frequency index")
plt.show()