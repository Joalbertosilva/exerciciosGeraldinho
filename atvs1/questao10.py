def fazer_perguntas():
    respostas = []
    
    perguntas = [
        "Telefonou para a vítima? ",
        "Esteve no local do crime? ",
        "Mora perto da vítima? ",
        "Tinha dívidas com a vítima? ",
        "Já trabalhou com a vítima? "
    ]
    
    for pergunta in perguntas:
        resposta = input(pergunta).lower()
        if resposta == 'sim' or resposta == 's':
            respostas.append(True)
        else:
            respostas.append(False)
    
    return respostas

def classificar_participacao(respostas):
    num_respostas_positivas = sum(respostas)
    
    if num_respostas_positivas == 2:
        return "Suspeita"
    elif 3 <= num_respostas_positivas <= 4:
        return "Cúmplice"
    elif num_respostas_positivas == 5:
        return "Assassino"
    else:
        return "Inocente"

def main():
    print("Responda às perguntas abaixo com 'sim' ou 'não'.")
    respostas = fazer_perguntas()
    
    classificacao = classificar_participacao(respostas)
    
    print(f"\nClassificação da participação no crime: {classificacao}")

if __name__ == "__main__":
    main()
