class Pilha:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

def empilhaP2(P, P2):
    while not P.is_empty():
        elemento = P.pop()
        if elemento is not None:
            P2.push(elemento)

def ler_e_empilhar(P):
    sequencia = input("Digite uma sequência de caracteres (ou 'fim' para encerrar): ")
    for char in sequencia:
        P.push(char)


def exibir_pilha(pilha, nome):
    print(f"Conteúdo da pilha {nome}:")
    while not pilha.is_empty():
        print(pilha.pop(), end=' ')
    print()

P = Pilha()
ler_e_empilhar(P)

P2 = Pilha()

empilhaP2(P, P2)

exibir_pilha(P, 'P')
exibir_pilha(P2, 'P2')
