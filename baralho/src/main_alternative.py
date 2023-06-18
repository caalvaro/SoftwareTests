def baralho1(entrada):
    cartas = []
    for i in range(0, len(entrada), 3):
        cartas = cartas + [entrada[i : i + 3]]

    cartas.sort()

    copas = 13
    espadas = 13
    ouros = 13
    paus = 13

    valor = "01"
    i = 0
    while valor != "14":
        while i < len(cartas) and cartas[i][:2] == valor:
            naipe = cartas[i][2]
            if naipe == "C":
                copas = copas - 1
            elif naipe == "E":
                espadas = espadas - 1
            elif naipe == "P":
                paus = paus - 1
            else:
                ouros = ouros - 1
            i = i + 1
        valor = str(int(valor) + 1)
        if len(valor) == 1:
            valor = "0" + valor
    return [copas, espadas, ouros, paus]


def main():
    entrada = input()
    resultado = baralho1(entrada)
    print(resultado[0])
    print(resultado[1])
    print(resultado[2])
    print(resultado[3])


main()
