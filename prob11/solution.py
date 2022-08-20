import numpy as np

A=np.loadtxt('lista_numeros.txt', dtype=int, delimiter=' ')

prod_l=0
prod_c=0
prod_d1=0
prod_d2=0

#numero de termos usados no produto
l=4

#testa o produto nas linhas
for i in range(A.shape[0]):
    for j in range(A.shape[1]-l+1):
        #linhas=A[i, j]*A[i, j+1]*A[i, j+2]*A[i, j+3]
        linhas=np.prod(A[i, j:j+l])
        if linhas>prod_l:
            prod_l=linhas

#testa o produto nas colunas
for j in range(A.shape[1]):
    for i in range(A.shape[0]-l+1):
        #colunas=A[i, j]*A[i+1, j]*A[i+2, j]*A[i+3, j]
        colunas=np.prod(A[i:i+l, j])
        if colunas>prod_c:
            prod_c=colunas

#testa o produto da diagonal principal
for i in range(A.shape[0]-l+1):
    for j in range(A.shape[1]-l+1):
        #diag_1=A[i, j]*A[i+1, j+1]*A[i+2, j+2]*A[i+3, j+3]
        idx = [(i+k, j+k) for k in range(l)]
        diag_1 = np.prod([A[m] for m in idx])
        if diag_1>prod_d1:
            prod_d1=diag_1

#testa o produto das diagonais secundáriSas
for i in range(A.shape[0]-l+1):
    for j in range(A.shape[1]-l+1):
        #diag_2=A[i+3, j]*A[i+2, j+1]*A[i+1, j+2]*A[i, j+3]
        idx = [(i+l-k-1, j+k) for k in range(l)]
        diag_2 = np.prod([A[m] for m in idx])
        if diag_2>prod_d2:
            prod_d2=diag_2


maximo=np.max([prod_l, prod_c, prod_d1, prod_d2])

print('maximo_produto={}'.format(maximo))