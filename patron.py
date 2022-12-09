patron = [["A","B","C"]
          ["D","E","F"]
          ["G","H","I"]]
def posibilidades_patron(inicial, patron):
    posibilidades = []
    for i in range(inicial, len(patron)):
        for j in range(len(patron[i])):
            if patron[i][j] == 0:
                posibilidades.append((i, j))
    return posibilidades
def resolver_patron(patron, posibilidades):
    if len(posibilidades) == 0:
        print(patron)
        return
    fila, columna = posibilidades[0]
    for k in range(1, 10):
        if es_valido(patron, fila, columna, k):
            patron[fila][columna] = k
            resolver_patron(patron, posibilidades_patron(1, patron))
            patron[fila][columna] = 0
    return patron
def es_valido(patron, fila, columna, numero):
    for i in range(len(patron)):
        if patron[fila][i] == numero:
            return False
        if patron[i][columna] == numero:
            return False
    for i in range(3):
        for j in range(3):
            if patron[(fila // 3) * 3 + i][(columna // 3) * 3 + j] == numero:
                return False
    return True
print(patron)
resolver_patron(patron, posibilidades_patron(0, patron))
print(patron)