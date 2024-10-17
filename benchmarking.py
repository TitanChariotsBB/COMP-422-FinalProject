import time

from oscillator import Oscillator
from dft import dft

NUM_TRIALS = 10

# Benchmark DFT
results = {}

n = 10
while n < 2000:
    results[n] = []
    res_sum = 0
    
    # Generate a 1 second signal of sample rate n
    osc = Oscillator(sample_rate=n, num_oscs=20)
    
    for i in range(NUM_TRIALS):
        osc.randomize()

        xt = [0.0] * n
        for i in range(n):
            xt[i] = osc.nextSample()
            
        # Time the DFT
        start = time.time()
        fxt = dft(xt)
        end = time.time()
        
        ms = (end - start) * 1000.0
        
        # results[n].append(ms)
        res_sum += ms
        
    results[n] = f"Avg: {round(res_sum / NUM_TRIALS, 5)} ms"
    
    n *= 10
    
print(results)