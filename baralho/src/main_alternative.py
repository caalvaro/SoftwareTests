def baralho1(entrada):
    cartas = []
    for i in range(0, len(entrada), 3):
        cartas = cartas + [entrada[i : i + 3]]

    cartas.sort()

    # refatoramos as variáveis para cada naipe para simplificar o código
    naipes = {
        "C": 13,
        "E": 13,
        "U": 13,
        "P": 13
    }

    valor = "01"
    i = 0
    while valor != "14":
        while i < len(cartas) and cartas[i][:2] == valor:
            naipe = cartas[i][2]
            # substituímos o if pelo get do dicionário
            naipes[naipe] -= 1
            
            i = i + 1
        valor = str(int(valor) + 1)
        if len(valor) == 1:
            valor = "0" + valor
    
    for i in range(1, len(cartas)):
        if cartas[i-1] == cartas[i]:
            naipe = cartas[i][2]
            naipes[naipe] = "erro"
  
    return list(naipes.values())


def main():
    entrada = input()
    resultado = baralho1(entrada)
    print(resultado[0])
    print(resultado[1])
    print(resultado[2])
    print(resultado[3])


main()
