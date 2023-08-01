# recebe uma lista x e devolve a média dos valores de x.
def media(x):
    soma = 0
    for i in range(len(x)):
        soma = x[i] + soma
    y = soma / len(x)
    return y

# recebe duas listas x e y e devolve a covariância entre x e y. Você deve usar a função media aqui.
def cov(x,y):
    medx = media(x)
    medy = media(y)
    soma = 0
    for i in range (len(x)):
        soma = ((x[i]-medx) * (y[i]-medy)) + soma
    coef = 1 / (len(x)-1)
    result = soma * coef
    return result
    

# recebe uma lista x e devolve o desvio padrão de x. Você deve usar a função media aqui.
def desvpad(x):
    med= media(x)
    soma = 0
    for i in range (len(x)):
        soma = ((x[i]-med)**2) + soma #somatoria dos quadradros das diferenças entre o termo e media
    n = len (x) #números de termos da sequencia menos 1
    coef = 1 / (n-1)  #coeficiente de multiplicação da somatória
    result = (coef * soma)**0.5
    return result


# recebe duas listas x e y e devolve o coeficiente de correlação de Pearson entre x e y.
# Você deve usar as funções cov e desvpad aqui.
def pearson(x,y):
    desvx = desvpad(x)
    desvy = desvpad(y)
    covar = cov(x,y)
    denominador = desvx * desvy
    coef = covar / denominador
    return coef

# recebe uma lista x e devolve o fractional ranking de x.
# Para o cálculo do posto, utilize o algoritmo de ordenação visto em aula.
# O posto de cada valor v distinto no vetor X é a média de suas 
# posições (iniciando no 1) na lista ordenada.
# Exemplo: [1.0, 1.0, 2.0, 3.0, 3.0, 4.0, 5.0, 5.0, 5.0]  (deve estar ordenado)
# * 1.0 -> (1+2)/2 = 1.5
# * 2.0 -> 3
# * 3.0 -> (4+5)/2 = 4.5
# * 4.0 -> 6
# * 5.0 -> (7+8+9)/3 = 8.0
def posto(x):
    postos_iniciais = []
    for i in range (len(x)):
        postos_iniciais.append(x[i])
    def ordenador_crescente_de_seq (seq):
        for i in range (len(seq)):
         for j in range (len(seq)):
             if seq[j]>seq[i]:
                 x = seq[i]
                 y = seq[j]
                 seq[i] = y
                 seq[j] = x
        return seq
    x = ordenador_crescente_de_seq(x) #ordenei a lista em ordem crescente
    postos_iniciais1 =[]
    for i in range (len(postos_iniciais)):
        postos_iniciais1.append(postos_iniciais[i])
    for i in range (len(x)):
        postos_iguais = []
        for j in range(len(x)):
            if x[i] == x[j]:
                postos_iguais.append(j) #achei, na lista ordenada, quais são os termos que se repetem e gravei seus indices em uma lista
        med = media(postos_iguais)#media dos indices (em ordem crescente) dos elementos que são iguais
        for k in range (len(postos_iguais)):
           for c in range (len(postos_iniciais1)):
                if x[postos_iguais[k]] == postos_iniciais1[c] and postos_iniciais1[c] == postos_iniciais[c]:#
                    postos_iniciais1[c] = med
    for i in range (len(postos_iniciais1)):
        postos_iniciais1[i] = postos_iniciais1[i] + 1
    return postos_iniciais1

# recebe duas listas x e y de devolve o coeficiente de correlação de Spearman entre x e y.
# Você deve usar a função Pearson aqui.
def spearman(x, y):
    def ordenador_crescente_de_seq (seq):
        for i in range (len(seq)):
         for j in range (len(seq)):
             if seq[j]>seq[i]:
                 x = seq[i]
                 y = seq[j]
                 seq[i] = y
                 seq[j] = x
        return seq
    listaX = posto(x)
    listaY = posto(y)
    spear = pearson(listaX, listaY)
    return spear


def matriz_correlacao(nome_arquivo, tipo_corr):
    arquivo = open (nome_arquivo, 'r')
    matriz_dados_inicial = []
    matriz_dados = []
    linha = arquivo.readline()
    while linha !='':
        linha = [linha]
        matriz_dados_inicial.append(linha)
        linha = arquivo.readline()
    arquivo.close()
    for i in range (1,len(matriz_dados_inicial[0])):
        linha = []
        for j in range (1,len(matriz_dados_inicial)):
            linha.append (matriz_dados_inicial[j][i])
        matriz_dados.append (linha) 
    if tipo_corr == 'cov':
        matriz_corr = []
        for i in range (len(matriz_dados)):
            linha = []
            for j in range(len(matriz_dados)):
                linha.append(cov(matriz_dados[i],matriz_dados[j]))
            matriz_corr.append(linha)
    elif tipo_corr == 'pearson':
        matriz_corr = []
        for i in range (len(matriz_dados)):
            linha = []
            for j in range(len(matriz_dados)):
                linha.append(pearson(matriz_dados[i],matriz_dados[j]))
            matriz_corr.append(linha)
    elif tipo_corr == 'spearman':
        matriz_corr = []
        for i in range (len(matriz_dados)):
            linha = []
            for j in range(len(matriz_dados)):
                linha.append(spearman(matriz_dados[i],matriz_dados[j]))
            matriz_corr.append(linha)
    return matriz_corr


# -----------------------------------------------------
# funções auxiliares prontas - Não devem ser alteradas
# -----------------------------------------------------

def imprime_lista(L):
    for elem in L:
        print("%.4f"%elem,end=" ")
    print()

def imprime_matriz(M):
    m = len(M)
    n = len(M[0])
    for i in range(m):
        for j in range(n):
            print("%14.4f"%(M[i][j]), end=" ")
        print()

# ------------------------------------------
# função principal - Não deve ser alterada
# ------------------------------------------
def main():
    modo = int(input("Digite o modo do programa: "))
    if modo == 1:
        n = int(input("Digite n: "))
        X = []
        for i in range(n):
            X.append(float(input("Digite x%d: "%(i+1))))
        print("media: %.4f"%(media(X)))
    elif modo == 2:
        n = int(input("Digite n: "))
        X = []
        for i in range(n):
            X.append(float(input("Digite x%d: "%(i+1))))
        print("desvpad: %.4f"%(desvpad(X)))
    elif modo == 3:
        n = int(input("Digite n: "))
        X = []
        for i in range(n):
            X.append(float(input("Digite x%d: "%(i+1))))
        Y = []
        for i in range(n):
            Y.append(float(input("Digite y%d: "%(i+1))))
        print("cov: %.4f"%(cov(X,Y)))
    elif modo == 4:
        n = int(input("Digite n: "))
        X = []
        for i in range(n):
            X.append(float(input("Digite x%d: "%(i+1))))
        Y = []
        for i in range(n):
            Y.append(float(input("Digite y%d: "%(i+1))))
        print("pearson: %.4f"%(pearson(X,Y)))
    elif modo == 5:
        n = int(input("Digite n: "))
        X = []
        for i in range(n):
            X.append(float(input("Digite x%d: "%(i+1))))
        P = posto(X)
        print("posto: ",end="")
        imprime_lista(P)
    elif modo == 6:
        n = int(input("Digite n: "))
        X = []
        for i in range(n):
            X.append(float(input("Digite x%d: "%(i+1))))
        Y = []
        for i in range(n):
            Y.append(float(input("Digite y%d: "%(i+1))))
        print("spearman: %.4f"%(spearman(X,Y)))
    elif modo == 7:
        nome_arquivo = input("Digite o nome do arquivo: ")
        tipo_corr = input("Digite a correlacao desejada: ")
        M = matriz_correlacao(nome_arquivo, tipo_corr)
        print("Matriz: ")
        imprime_matriz(M)

        
#Não altere o código abaixo:
if __name__ == "__main__":
	main()