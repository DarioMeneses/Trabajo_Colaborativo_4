# Ejemplo Matrices
chess_board = [
['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
[ 0,   0,   0,   0,   0,   0,   0,   0],
[ 0,   0,   0,   0,   0,   0,   0,   0],
[ 0,   0,   0,   0,   0,   0,   0,   0],
[ 0,   0,   0,   0,   0,   0,   0,   0],
['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]
chess_board[7][1] = 0 # Casilla original del caballo ahora está vacía
chess_board[5][2] = 'N' # Nueva posición del caballo

chess_board[1][1] = 0 # La casilla del peon esta vacia
chess_board[3][1] = "p" # Nueva posicion del peon 

for chess in chess_board:
    print(chess)

