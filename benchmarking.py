import time

from oscillator import Oscillator
from dft import dft
from fft import fft

NUM_TRIALS = 10

# Benchmark DFT
dft_results = {}
fft_results = {}

n = 256
while n < 5000:
    print(f"Benchmarking n={n}")
    
    dft_results[n] = []
    dft_res_sum = 0

    fft_results[n] = []
    fft_res_sum = 0
    
    # Generate a 1 second signal of sample rate n
    osc = Oscillator(sample_rate=n, num_oscs=20)
    
    for i in range(NUM_TRIALS):
        osc.randomize()

        xt = [0.0] * n
        for i in range(n):
            xt[i] = osc.nextSample()
            
        # Time the DFT
        dft_start = time.time()
        dft_fxt = dft(xt)
        dft_end = time.time()
        
        dft_ms = (dft_end - dft_start) * 1000.0

        # Time the FFT
        fft_start = time.time()
        fft_fxt = fft(xt)
        fft_end = time.time()
        
        fft_ms = (fft_end - fft_start) * 1000.0
        
        # results[n].append(ms)
        dft_res_sum += dft_ms
        fft_res_sum += fft_ms
        
    dft_results[n] = f"Avg: {round(dft_res_sum / NUM_TRIALS, 4)} ms"
    fft_results[n] = f"Avg: {round(fft_res_sum / NUM_TRIALS, 4)} ms"
    
    n *= 2
    
print(f"DFT: {dft_results}")
print(f"FFT: {fft_results}")