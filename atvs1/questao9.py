def calcular_estatisticas_notas(notas):
    quantidade = len(notas)
    print(f"Quantidade de notas lidas: {quantidade}")
    
    print("Notas na ordem em que foram informadas:")
    for nota in notas:
        print(nota)
    
    print("Notas na ordem inversa:")
    for nota in reversed(notas):
        print(nota)
    
    soma_notas = sum(notas)
    print(f"Soma das notas: {soma_notas}")
    
    media_notas = soma_notas / quantidade if quantidade > 0 else 0
    print(f"Média das notas: {media_notas}")
    
    acima_da_media = [nota for nota in notas if nota > media_notas]
    quantidade_acima_da_media = len(acima_da_media)
    print(f"Quantidade de notas acima da média: {quantidade_acima_da_media}")

def main():
    notas = []
    
    while True:
        nota_str = input("Digite uma nota (ou 'fim' para encerrar): ")
        
        if nota_str.lower() == 'fim':
            break
        
        try:
            nota = float(nota_str)
            notas.append(nota)
        except ValueError:
            print("Valor inválido. Digite um número válido ou 'fim' para encerrar.")
    
    if notas:
        calcular_estatisticas_notas(notas)
    else:
        print("Nenhuma nota foi inserida.")

if __name__ == "__main__":
    main()
