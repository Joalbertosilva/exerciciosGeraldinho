
def registro_(nome, protocolo, assunto):
    registro = {
        'Nome': nome,
        'Protocolo': protocolo,
        'Assunto': assunto
    }
    return registro  
def atender(registro):
    print('Cliente atendido:', registro['Nome'])
def mostrar(registros):
    print('Registros pendentes:')
    for registro in registros:
        print(registro)
registros_pendentes = []
