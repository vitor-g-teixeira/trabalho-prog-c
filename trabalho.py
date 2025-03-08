def comprimir(matriz):
    comprido_vetor = []

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            comprido_vetor.append(matriz[i][j])

    result = []
    i = 0

    while i < len(comprido_vetor):

        currentTupla = [1, comprido_vetor[i]]

        if i + 1 > len(comprido_vetor) - 1:
            result.append(currentTupla)
            break

        elif comprido_vetor[i] == comprido_vetor[i + 1]:
            while comprido_vetor[i] == comprido_vetor[i + 1]:
                currentTupla[0] += 1
                i += 1
                if i + 1 >= len(comprido_vetor):
                    break
            result.append(currentTupla)

            if i + 1 <= len(comprido_vetor) - 1:
                i += 1
            else: 
                break
        else:
            result.append(currentTupla)
            i += 1
    return result

def descomprimir(RLEcode, rowAmount, colAmount):
    resultMatrix = [[0]*colAmount for _ in range(rowAmount)]
    currentRow = 0
    currentCol = 0

    for tupla in RLEcode:
        if currentRow >= len(resultMatrix):
            break
        insertAmount = tupla[0]
        toInsertValue = tupla[1]

        for _ in range(insertAmount):
            resultMatrix[currentRow][currentCol] = toInsertValue
            currentCol += 1
            if currentCol == colAmount:
                currentRow += 1
                currentCol = 0

    return resultMatrix

def matrizador(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()

matriz = [[1, 1, 2, 3], [3, 4, 4, 5], [5, 5, 5, 5]]
matrizador(matriz)

RLEcode = comprimir(matriz)
print(RLEcode)

matriz_descomprimida = descomprimir(RLEcode, 3, 4)
matrizador(matriz_descomprimida)