def baralho1(entrada):
    cartas = []
    for i in range(0, len(entrada), 3):
        cartas = cartas + [entrada[i : i + 3]]

    cartas.sort()

    naipes = {"C": 13, "E": 13, "U": 13, "P": 13}

    i = 0
    for valor in range(1, 14):
        while i < len(cartas) and int(cartas[i][:2]) == valor:
            naipe = cartas[i][2]
            naipes[naipe] -= 1
            i = i + 1

    for i in range(1, len(cartas)):
        if cartas[i - 1] == cartas[i]:
            naipe = cartas[i][2]
            naipes[naipe] = "erro"

    return list(naipes.values())
