
fila = []
def insere(n, f = fila): f.append(n) 
def remove(f = fila): f.pop(0)
def primeiroDaFila(f=fila): return f[0]
def tamanho(f = fila): return len(f)
def filaVazia(f = fila): return (len(f) == 0)
def mostrarFila(f = fila):
    for nome in f: print(nome)