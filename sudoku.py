sudoku1 = [
           [5, 0, 0, 0, 4, 0, 0, 0, 9],
           [0, 2, 0, 0, 1, 0, 6, 8, 0],
           [0, 0, 9, 8, 7, 0, 1, 0, 0],
           [0, 0, 6, 7, 0, 0, 2, 0, 0],
           [0, 9, 0, 3, 5, 4, 0, 6, 0],
           [3, 0, 0, 0, 0, 0, 0, 0, 1],
           [9, 0, 0, 0, 6, 0, 0, 0, 2],
           [0, 1, 4, 0, 3, 0, 0, 5, 7],
           [0, 0, 5, 0, 8, 7, 0, 0, 0]  
    ]    
def es_valido(sudoku, fila, columna, numero):
    for i in range(len(sudoku)):
        if sudoku[fila][i] == numero:
            return False
        if sudoku[i][columna] == numero:
            return False
    for i in range(3):
        for j in range(3):
            if sudoku[(fila // 3) * 3 + i][(columna // 3) * 3 + j] == numero:
                return False
    return True
def resolver_sudokus(sudoku):
    posibilidades = []
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                posibilidades.append((i, j))
    if len(posibilidades) == 0:
        print(sudoku)
        return
    fila, columna = posibilidades[0]
    for k in range(1, 10):
        if es_valido(sudoku, fila, columna, k):
            sudoku[fila][columna] = k
            resolver_sudokus(sudoku)
            sudoku[fila][columna] = 0
    return sudoku
resolver_sudokus(sudoku1)
