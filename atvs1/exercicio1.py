

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def lista1():
    for i in range (1, 10):
        print(i)
def lista2():
    for i in range(8, 14):
        print(i)
def lista3():
    for i in range(0, 16, 2):
        print(i)
def lista4():
    for i in range(1, 16, 2):
        print(i)
def lista5():
    print('Os múltiplos de 2 são:')
    for i in range(2, 16, 2):
        print(i)
    print('Os múltiplos de 3 são:')
    for i in range(3, 16, 3):
        print(i)
    print('Os múltiplos de 4 são:')
    for i in range(4, 16, 4):
        print(i)
def lista6():
    for i in range(15, 0, -1):
        print(i)
def lista7():
    numeros = list(range(16))
    soma = 0.0
    for num in numeros[10:16]:
        if 3 <= num <= 9:
            soma += float(num)
    print(f'A soma dos números de 10 a 15 no intervalo de 3 a 9 em float é: {soma}')

