# COMP 422 FinalProject

### Installing dependencies for `testing.py`

`python -m pip install numpy matplotlib`

### How to use `fourier-learning.py`

This script creates a 1 second sine wave (and the second harmonic) with a given sample rate (arg 1) and frequency (arg 2). It plots the first 2 cycles of the sample to show the waveform, then it plots the absolute value (magnitude) of the positive half of the DFT.

Example: `python fourier-learning.py 44100 220`

### How to use `dft-testing.py`

This script creates 1 second of audio wave at a given sample rate (arg 1) and number of oscilators frequency (arg 2). It plots a snapsnot of the waveform, then it plots the absolute value (magnitude) of the positive half of the DFT.

Example: `python fourier-learning.py 1500 10`

### TODO

* [x] Implement vanilla DFT
* [ ] Implement FFT
* [x] Write a program which adds many random frequency partials to signal
* [ ] Benchmark algorithms at various sample rates (our n in this case)
