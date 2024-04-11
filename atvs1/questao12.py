print('Qual o melhor Sistema Operacional para uso em servidores?')
print('''1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro''')

opcoes = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
sistemas = [0] * 6
while True:
    while True:
        opcao = int(input('Digite a opção: '))
        if opcao > 6 or opcao < 0:
            print('Opção inválida.')
        else:
            break
    if opcao == 0:
        break
    sistemas[opcao - 1] = sistemas[opcao - 1] + 1


print('Sistema Operacional     Votos  %')
print('----------------------------------')
cont = 0
melhor = 0
melhorSis = ''
perc = 0
for s in sistemas:
    print('%s   %d   %.2f%%' % (opcoes[cont], s,(s * 100) / sum(sistemas) ))
    if s > melhor:
        melhor = s
        melhorSis = opcoes[cont]
        perc = (s * 100) / sum(sistemas)
    cont += 1

print('----------------------------------')
print('Total   %d' % sum(sistemas))
print('O Sistema Operacional mais votado foi o %s, com %d votos, correspondendo a %.2f dos votos.' % (melhorSis, melhor, perc))
    
