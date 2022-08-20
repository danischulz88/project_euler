import sys
sys.path.append('..')
import numpy as np
import biblioteca as bib

primos=[2]

while primos[-1]<2e6:
    primos=bib.crivo(primos)
    print(primos[-1])

soma=np.sum(primos[:-1])
print('soma ={}'.format(soma))