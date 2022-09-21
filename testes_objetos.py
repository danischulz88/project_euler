import re


class Racionais:
    def __init__(self, num, den):
        self.num=num
        self.den=den

    def __str__(self):
        return f'{self.num}/{self.den}'
    
    def __mul__(self, other):
        num=self.num*other.num
        den=self.den*other.den
        return Racionais(num, den)
    
    def __floordiv__(self, other):
        num=self.num*other.den
        den=self.den*other.num
        return Racionais(num, den)
    
    def __add__(self, other):
        num=self.num*other.den+other.num*self.den
        den=self.den*other.den
        return Racionais(num, den)
    

numero1=Racionais(1, 2)
numero2=Racionais(2, 3)


print(numero1+numero2)