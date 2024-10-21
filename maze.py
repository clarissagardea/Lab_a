# Clarissa Gardea Coronado
# A01569420

# Programa con el algoritmo de backtracking para encontrar el camino hacia la salida de un laberinto
# Conclusion: El algoritmo de back tracking y la recursividad se usa comunmente para encontrar todas las soluciones posibles
# pero esot lo hace muy ineficiente y no seria optimo implementarlo en muchos casos, a menos de que no nos importen la cantidad de
# tiempo o recusros usados.

def print_maze(maze):
    for row in maze:
        for col in row:
            if col == 0:
                print('0', end="   ")  # Pared
            elif col == 1:
                print('1', end="   ")  # Posible camino
            elif col == 2:
                print('S', end="   ")  # Inicio
            elif col == 3:
                print('E', end="   ")  # Final
            elif col == '*':
                print('*', end="   ")  # Por aqui si
            elif col == 'X':
                print('X', end="   ")  # Callejon sin salida
        print()

def position(maze, symbol):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == symbol:
                return row, col
    return None

def solve_maze(maze, row, col):
    # Caso base: encuentra salida(3)
    if maze[row][col] == 3:
        return True

    #Marcar camino de la solucion
    maze[row][col] = '*'

    # Declaracion de movimientos:arriba, abajo, izquierda y derecha
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for direction in directions:
        new_row, new_col = row + direction[0], col + direction[1]

        #ver si se puede seguir en la posicion o si es salida
        if (0 <= new_row < len(maze) and 0 <= new_col < len(maze[0])
            and (maze[new_row][new_col] == 1 or maze[new_row][new_col] == 3)):
            
            if solve_maze(maze, new_row, new_col):
                return True

    # si no se puede seguir, marca como no valida y se regresa
    maze[row][col] = 'X'
    return False

# Diseño del maze 
maze = [
[2,  1,  1,  0,  0,  1,  1,  1,  0,  0],
[0,  1,  0,  1,  1,  1,  0,  1,  0,  0],
[0,  1,  1,  1,  0,  0,  0,  1,  0,  0],
[0,  1,  0,  1,  0,  0,  1,  1,  1,  0],
[1,  1,  0,  1,  0,  1,  1,  0,  1,  0],
[0,  0,  0,  0,  0,  1,  0,  1,  1,  0],
[0,  1,  1,  1,  1,  1,  0,  1,  0,  0],
[1,  1,  0,  0,  1,  0,  1,  1,  1,  0],
[1,  0,  1,  1,  1,  1,  1,  0,  1,  3],
[1,  0,  0,  0,  0,  0,  0,  0,  0,  0]
]

print("Initial Maze:")
print_maze(maze)

# posicion inicial
start_row, start_col = position(maze, 2)

# solucion 
if solve_maze(maze, start_row, start_col):
    print("\nSolution found:")
else:
    print("\nNo solution exists")

print_maze(maze)
