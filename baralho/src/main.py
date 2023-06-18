def baralho2(entrada):
    print(1)
    cartas = {"C": [], "E": [], "U": [], "P": []}

    for i in range(0, len(entrada), 3):
        print(2)
        chave = entrada[i + 2]
        cartas[chave] = cartas[chave] + [int(entrada[i : i + 2])]
        print(3)

    print(4)
    faltam = {"C": 13, "E": 13, "U": 13, "P": 13}

    for naipe in ["C", "E", "U", "P"]:
        print(5)
        print(6)
        for valor in range(1, 13):
            print(7)
            print(8)
            qtd = cartas[naipe].count(valor)
            if qtd > 1:
                print(9)
                faltam[naipe] = "erro"
            elif qtd == 1 and faltam[naipe] != "erro":
                print(10)
                print(11)
                faltam[naipe] -= 1
            print(12)
        print(13)

    print(14)
    return [faltam["C"], faltam["E"], faltam["U"], faltam["P"]]


def main():
    entrada = input()
    resultado = baralho2(entrada)
    print(resultado[0])
    print(resultado[1])
    print(resultado[2])
    print(resultado[3])


main()
