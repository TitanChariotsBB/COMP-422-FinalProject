import sys
import math
import numpy as np
import matplotlib.pyplot as plt

from oscillator import Oscillator

if len(sys.argv) > 1:
    try:
        sample_rate = int(sys.argv[1])
    except:
        sample_rate = 1000
else:
    sample_rate = 1000
    
if len(sys.argv) > 2:
    try:
        num_oscs = int(sys.argv[2])
    except:
        num_oscs = 10
else:
    num_oscs = 10
        

# define x(t) as sine wave at the given freq
xt = np.zeros(sample_rate) # initialize buffer

osc = Oscillator(sample_rate, num_oscs)

# freq_array = osc.randomize()
# print(freq_array)

freq_array = osc.overtones(220)
print(freq_array)

# fill the buffer with samples of the wave
for i in range(xt.size):
    xt[i] = osc.nextSample()

# Plot the first n samples of the signal
plt.plot(xt[:440])
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