import numpy  as np
# calcula o  produto da unica terna pitagorica tal que a+b+c=1000
#considerando que a^2+b^2=c^2 (1) e que a+b+c=1000 (2), isolamos c na equacao (2)
#gerando uma relação entre os valores de a e b. Assim podemos gerar a em funcao de b
#o que gera o seguinte programa
for b in range(1, 500):
    resto=(5e5-1e3*b)%(1e3-b)
    if resto==0:
        a=int((5e5-1e3*b)/(1e3-b))
        c=1000-a-b
        print('a={}, b={}, c={}'.format(a, b, c))
        print('soma={}, produto={}'.format(a+b+c, a*b*c))

