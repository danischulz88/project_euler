from math import floor, log, sqrt

# funcao que estima posicao da sequencia com termo menor que m
def estima_n(m):
    phi=(1+sqrt(5))/2
    n=1+((log(m)-log(2))/(3*log(phi)))
    return floor(n)

m=4e6

print("estimando n")
n=estima_n(m)
print("n={}".format(n))

# valores iniciais da sequencia dos termos pares da sequencia de fibonacci
ba=2
bb=8

#s1=ba+bb
s=10 

# gera os proximos termos pares da sequencia e calcula a soma deles
for i in range(3, n+1):
    bn=4*bb+ba
    s=bn+s
    ba=bb
    bb=bn

print("n={}, bn={}".format(n, bn))
print("soma={}".format(s))