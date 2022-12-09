sudoku1 = [[5, 0, 0, 0, 4, 0, 0, 0, 9],
           [0, 2, 0, 0, 1, 0, 6, 8, 0],
           [0, 0, 9, 8, 7, 0, 1, 0, 0],
           [0, 0, 6, 7, 0, 0, 2, 0, 0],
           [0, 9, 0, 3, 5, 4, 0, 6, 0],
           [3, 0, 0, 0, 0, 0, 0, 0, 1],
           [9, 0, 0, 0, 6, 0, 0, 0, 2]
           [0, 1, 4, 0, 3, 0, 0, 5, 7],
           [0, 0, 5, 0, 8, 7, 0, 0, 0],]
def resolver_sudokus(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for k in range(1, 10):
                    if es_valido(sudoku, i, j, k):
                        sudoku[i][j] = k
                        resolver_sudokus(sudoku)
                        sudoku[i][j] = 0
                return sudoku
                
def es_valido(sudoku, fila, columna, numero):
    for i in range(9):
        if sudoku[fila][i] == numero:
            return False
        if sudoku[i][columna] == numero:
            return False
    for i in range(3):
        for j in range(3):
            if sudoku[(fila // 3) * 3 + i][(columna // 3) * 3 + j] == numero:
                return False
    return True
resolver_sudokus(sudoku1)
