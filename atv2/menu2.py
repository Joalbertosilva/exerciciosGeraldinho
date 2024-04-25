from atv2.fila2 import *
import random


print('Atendimento de clientes')

while True:
    opc = int(input('1 - Inserir cliente\n2 - Atender cliente\n3 - Mostrar atendimentos pendentes\n4 - Encerrar\nEscolha uma opção: '))
    if opc == 1:
        nome = input('Digite o nome do cliente: ')
        protocolo = random.randint(1, 1000) 
        assunto = input('Assunto: ')
        novo_registro = registro_(nome, protocolo, assunto)
        registros_pendentes.append(novo_registro) 
    elif opc == 2:
        if len(registros_pendentes) > 0:
            cliente_atender = registros_pendentes.pop(0)  
            atender(cliente_atender)
            print('Cliente atendido: ', cliente_atender['Nome'], '| Assunto: ', cliente_atender['Assunto'])
        else:
            print('Não há clientes para atender.')
    elif opc == 3:
        if len(registros_pendentes) > 0:
            mostrar(registros_pendentes)
        else:
            print('Não há registros pendentes.')
    elif opc == 4:
        print('Encerrando o programa.')
        break
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')
