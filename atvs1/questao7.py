

def criar_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = i * num_colunas + j + 1
            linha.append(valor)
        matriz.append(linha)
    return matriz

def mostrar_matriz(matriz):
    for linha in matriz:
        print(linha)

def main():
    try:
        num_linhas = int(input('Digite o número de linhas da matriz: '))
        num_colunas = int(input('Digite o número de colunas da matriz: '))
        
        if num_linhas <= 0 or num_colunas <= 0:
            print('Por favor, insira valores positivos para o número de linhas e colunas.')
            return
        
        matriz = criar_matriz(num_linhas, num_colunas)
        print('Matriz criada:')
        mostrar_matriz(matriz)
    
    except ValueError:
        print('Entrada inválida. Certifique-se de digitar um número inteiro válido.')

if __name__ == "__main__":
    main()
