from fila import *

print('Atendimento de clientes')
enter = '\n....Digite ENTER'
while True:
    opc = int(input('  1 - Inserir Cliente\n  2 - Mostrar primeiro da fila\n  3 - Atender cliente\n  4 - Mostrar tamanho da fila\n  5 - Encerrar\n Escolha uma opção: '))

    if opc == 1:
        nome = input('Digite o nome do cliente: ')
        insere(nome)
    elif opc == 2:
        if filaVazia():
            print('Não há clientes na fila')
        else:
            print('Primeiro da fila: ', primeiroDaFila())
    elif opc == 3:
        if filaVazia():
            print('Não há lientes na fila')
        else:
            print('Cliente atendido: ', remove())
    elif opc == 4:
        print('Tamanho atual da fila: ', tamanho(), enter)
    elif opc == 5:
        break
    else:
        print('Opção inválida', enter)
    if filaVazia():
        print('Todos os clientes foram atendidos')
    else:
        print('Clientes não atendidos')
        mostrarFila()