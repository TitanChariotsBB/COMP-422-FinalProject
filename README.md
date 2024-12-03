# COMP 422 FinalProject

### Installing dependencies for `testing.py`

`python -m pip install numpy matplotlib`

### How to use `correctness.py`

This script demonstrates that the DFT and FFT correctly detect the component frequencies of a randomly generated 1 second signal.

Base usage: `python correctness.py`

With custom sample rate, oscilator count, and mode: `python correctness.py 1024 30 random`

### How to use `benchmarking.py`

For problem sizes of 256, 512, 1024, 2048, and 4096, this script measures the performance of the DFT and FFT 10 times each and averages the results.

Usage: `python benchmarking.py`

### What is oscillator.py?

This class creates a 1 second signal at a given sample rate. It creates the signal by summing sine waves at various frequencies and amplitudes. The random mode randomizes both frequencies and amplitudes, and the overtones mode creates a fundamental signal and adds its overtones at random amplitudes.
