import random
import numpy as np

# Multi voice additive oscillator
class Oscillator:
    sample_rate: int
    num_oscs: int
    
    def __init__(self, sample_rate, num_oscs) -> None:
        self.sample_rate = sample_rate
        self.num_oscs = num_oscs
        self.amps = [0.0] * num_oscs
        self.freqs = [0.0] * num_oscs 
        self.incs = [0.0] * num_oscs
        self.ts = [0.0] * num_oscs
        
    def randomize(self):
        for i in range(self.num_oscs):
            # random amplitude [0, 1)
            self.amps[i] = random.random()
            
            # random frequency [40, Nyquist)
            freq = random.random() * ((self.sample_rate / 2) - 40) + 40
            self.freqs[i] = freq
            inc = 2 * np.pi * freq / self.sample_rate
            self.incs[i] = inc
            
    def nextSample(self):
        sum = 0.0
        for i in range(self.num_oscs):
            sum += np.sin(self.ts[i]) * self.amps[i]
            self.ts[i] += self.incs[i]
        return sum