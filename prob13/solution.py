import numpy as np

class Inteiro:
    #entra com lista de caracteres e transforma num array considerando cada caracter como um inteiro
    #considerando a lista de tras para frente
    def __init__(self, str):
        self.digitos=np.array([d for d in str[::-1]], dtype=int)

    #intrime os valores do array desfazendo a inversão de ordem
    def __str__(self):
        return f'{self.digitos[::-1]}'
    
    def __add__(self, other):
        if self.digitos.size>other.digitos.size:
            m=self.digitos.size
            n=other.digitos.size
        else:
            m=other.digitos.size
            n=self.digitos.size
        resultado = Inteiro('')
        resultado.digitos = np.zeros(m, dtype=int)
        
        return resultado

#with open("dados.txt") as file:
#    lines=file.readlines()
#    lines=[line.rstrip() for line in lines]
#    print(lines)

digitos=np.zeros(4, dtype=int)
print(digitos)
