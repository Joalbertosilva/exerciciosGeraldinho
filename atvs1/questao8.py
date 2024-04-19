def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = int(input(f'Digite o valor para M[{i}][{j}]: '))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def dobrar_valores(matriz):
    matriz_dobrada = []
    for linha in matriz:
        linha_dobrada = [2 * valor for valor in linha]
        matriz_dobrada.append(linha_dobrada)
    return matriz_dobrada

def exibir_matriz(matriz):
    for linha in matriz:
        print(linha)

linhas = int(input('Digite o número de linhas da matriz: '))
colunas = int(input('Digite o número de colunas da matriz: '))

matriz_original = criar_matriz(linhas, colunas)

matriz_dobrada = dobrar_valores(matriz_original)

print('\nMatriz original:')
exibir_matriz(matriz_original)

print('\nMatriz com o dobro dos valores:')
exibir_matriz(matriz_dobrada)
