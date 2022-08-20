import sys
sys.path.append('..')
import numpy as np
import biblioteca as bib

primes = np.array([2], dtype=np.int64)

for _ in range(10000):
    primes = bib.crivo(primes)

print(primes.size)
print(primes[-1])