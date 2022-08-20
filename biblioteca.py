import numpy as np

#=================================================================================
#                 Crivo dos numeros primos
#=================================================================================
def crivo(primos):
    # primos[-1] pega o último primo da lista
    p_teste=primos[-1]+1
    # usa false para entrar no while
    p_primo=False
    while not p_primo:
        # supoe que o valor testado é primo 
        p_primo=True
        for p in primos:
            if p_teste%p==0:
                # se nao for primo troca para false para rodar novamente
                p_primo=False
                # e testa o proximo numero natural
                p_teste=p_teste+1
                break  
    # acrescente o proximo primo na lista
    primos=np.append(primos, p_teste)
    return primos

#=========================================================================
#            calcula o mmc de uma lista de valores
#=========================================================================
def mmc(valores):
    #inicia multiplicadores
    resultado=1
    #inicia lista de primos
    primos=np.array([2])
    #remove valores iguais a 1 da lista para o mmc
    #cria um vetor vazio
    remove=np.array([], dtype=np.int64)
    for k in range(valores.size):
        #verifica se algum termo é igual a 1
        if valores[k]==1:
            #armazena as posicoes dos termos igual a 1
            remove=np.append(remove, k)
    #limpa da lista os valores
    valores=np.delete(valores, remove)

    #enquanto houverem valores para o teste
    while valores.size != 0:
        divisor=False
        remove=np.array([], dtype=np.int64)
        for k in range(valores.size):
            #testa se o valor tem fator primo
            if valores[k]%primos[-1]==0:
                #simplifica o valor na lista
                valores[k]=valores[k]//primos[-1]
                #salva o fator primo para construir o mmc
                divisor=True
                #verifica se o termo já foi fatorado
                if valores[k]==1:
                     #armazena as posicoes dos termos igual a 1
                    remove=np.append(remove, k)
         #limpa da lista os valores iguais a 1
        valores=np.delete(valores, remove)
        # verifica se o ultimo fator primo foi utilizado
        if divisor:
            #acumula o mmc
            resultado=resultado*primos[-1]
        else:
            # gera o proximo primo
            primos=crivo(primos)
    return resultado

#=========================================================================
#            numero de divisores de um número inteiro
#=========================================================================
def divisores(n):
    n_sqrt=np.sqrt(n)
    n_floor=int(np.floor(n_sqrt))
    #testa se o número tem raiz inteira, se sim pega a raiz como máximo valor
    #de teste, caso contrario pega o maior inteiro possível
    if n_sqrt==n_floor:
        k_max=int(n_sqrt)-1
        j=1
    else:
        k_max=n_floor
        j=0

    n_div=0

    for i in range(2, k_max+1):
        if n%i==0:
            n_div+=1
    
    return 2*(n_div+1)+j
