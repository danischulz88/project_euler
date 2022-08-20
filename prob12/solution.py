import numpy as np
import sys
sys.path.append('..')
import biblioteca as bib

triangular=0
n_div=0
k=0

#testa enquanto não atingir o numero de divisores desejado
while n_div<=500:
    k+=1
    triangular+=k
    n_div=bib.divisores(triangular)

print('k={}, triang={}, n_div={}'.format(k, triangular, n_div))