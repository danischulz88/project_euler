import numpy as np
#dada uma sequencia de números calcula o maior produto de l fatores

#entra com a sequencia
DIGITS ='73167176531330624919225119674426574742355349194934'\
        '96983520312774506326239578318016984801869478851843'\
        '85861560789112949495459501737958331952853208805511'\
        '12540698747158523863050715693290963295227443043557'\
        '66896648950445244523161731856403098711121722383113'\
        '62229893423380308135336276614282806444486645238749'\
        '30358907296290491560440772390713810515859307960866'\
        '70172427121883998797908792274921901699720888093776'\
        '65727333001053367881220235421809751254540594752243'\
        '52584907711670556013604839586446706324415722155397'\
        '53697817977846174064955149290862569321978468622482'\
        '83972241375657056057490261407972968652414535100474'\
        '82166370484403199890008895243450658541227588666881'\
        '16427171479924442928230863465674813919123162824586'\
        '17866458359124566529476545682848912883142607690042'\
        '24219022671055626321111109370544217506941658960408'\
        '07198403850962455444362981230987879927244284909188'\
        '84580156166097919133875499200524063689912560717606'\
        '05886116467109405077541002256983155200055935729725'\
        '71636269561882670428252483600823257530420752963450'

#quebra a sequencia antes e depois de cada zero, considerando que
#se ha um zero o produto será zero
subsequencia=DIGITS.split('0')

#numero de elementos que se quer multiplicar
l=13

 #cria um vetor vazio
remove=np.array([], dtype=np.int64)
for k in range(len(subsequencia)):
    #verifica se alguma sequencia tem menos que l elementos
    if len(subsequencia[k])<l:
        #armazena as posicoes dessas sequencias
        remove=np.append(remove, k)
#limpa da lista as sequencias pequenas
subsequencia=np.delete(np.array(subsequencia), remove)

maximo_produto=0

for x in subsequencia:
    #quebra a string em valores
    a=np.fromiter(x, dtype=int)
    #calcula o produto dos l primeiros elementos da sequencia
    prod=np.prod(a[:l])
    if prod>maximo_produto:
        maximo_produto=prod
    for i in range(a.size-l):
        #calcula os proximos produtos desconsiderando o primeiro 
        #valor da sequencia anterior e acrescentando um proximo
        prod=prod*a[i+l]//a[i]
        if prod>maximo_produto:
            maximo_produto=prod
print(maximo_produto)