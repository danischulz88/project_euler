import numpy as np

contador_max=1
#testa os valores de 3 a 1 milhão
for n0 in range(3, 1_000_000):
    n=n0
    contador=1
    while n != 1:
        contador+=1
        if n % 2 == 0:
            n=n//2
        else:
            n=3*n+1
    
    if contador>contador_max:
        contador_max=contador
        numero=n0  

print(f'{contador_max =}, {numero =}')  
