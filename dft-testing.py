from dft import dft
from fft import fft

import sys
import math
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
xt = [0.0] * sample_rate # initialize buffer

osc = Oscillator(sample_rate, num_oscs)

# Random frequencies
# freq_array = osc.randomize()
# print(freq_array)

# Random amplitudes of harmonic series
freq_array = osc.overtones(220)
print(freq_array)

# fill the buffer with samples of the wave
for i in range(len(xt)):
    xt[i] = osc.nextSample()

# Plot the first two cycles of the signal
two_cycles_index = math.ceil(2 * (sample_rate / 220))
plt.plot(xt[:two_cycles_index])
plt.title("Sample index")
plt.ylabel("Value of x(t)")
plt.show()

# Plot the absolute value (magnitude) of the dft
fxt = dft(xt)
pos_freq_bound = math.ceil(len(fxt) / 2) + 1
pos_fxt_mag = fxt[:pos_freq_bound]
plt.plot(pos_fxt_mag)
plt.xscale("log")
plt.title("Absolute value of the DFT of x(t)")
plt.ylabel("Magnitude")
plt.xlabel("Frequency index")
plt.show()

# Plot the absolute value (magnitude) of the fft
fxt = fft(xt)
pos_freq_bound = math.ceil(len(fxt) / 2) + 1
pos_fxt_mag = fxt[:pos_freq_bound]
plt.plot(pos_fxt_mag)
plt.xscale("log")
plt.title("Absolute value of the FFT of x(t)")
plt.ylabel("Magnitude")
plt.xlabel("Frequency index")
plt.show()