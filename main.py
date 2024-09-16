"""
Alumnos:
Morales Ramos Bernardo. 1288710
Arce Montoya José Antonio. 1271264
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk

# Variables globales que se usarán en todo el programa
tablero = [[False for j in range(8)] for i in range(8)]
tablero_completo = False
solucion = []

for i in range(8):
  print(tablero[i])

def esta_completo(tablero, tablero_completo):
  if tablero_completo == True:
    return True

  for i in range(8):
    for j in range(8):
      if tablero[i][j] == False:
        return False

  tablero_completo = True
  return True

def es_casilla_valida(i_ev, j_ev):
  if i_ev >= 0 and j_ev >= 0:
    if i_ev <= 7 and j_ev <= 7:
      if tablero[i_ev][j_ev] == False:
        # print(f"({i_ev},{j_ev}) fueron validas")
        return True
  return False

def casillas_validas(i, j):
  casillas = []

  if es_casilla_valida(i-2, j+1):
    casillas.append([i-2, j+1])

  if es_casilla_valida(i-1, j+2):
    casillas.append([i-1, j+2])

  if es_casilla_valida(i+1, j+2):
    casillas.append([i+1, j+2])

  if es_casilla_valida(i+2, j+1):
    casillas.append([i+2, j+1])

  if es_casilla_valida(i+2, j-1):
    casillas.append([i+2, j-1])

  if es_casilla_valida(i+1, j-2):
    casillas.append([i+1, j-2])

  if es_casilla_valida(i-1, j-2):
    casillas.append([i-1, j-2])

  if es_casilla_valida(i-2, j-1):
    casillas.append([i-2, j-1])

  return casillas

def backtracking_caballo(coord_i, coord_j):
  # print(f'Llamada recursiva en ({coord_i}, {coord_j})')

  # Marcar la casilla en la que estamos
  tablero[coord_i][coord_j] = True

  # Agregar a la solucion final
  solucion.append((coord_i, coord_j))

  # Obtener las casillas validas en base a donde estamos
  casillas = casillas_validas(coord_i, coord_j)

  # Una lista vacía es False.
  if not casillas: # Si la lista está vacía, es un camino perdido o completo
    # print("Esta llamada no tiene mas casillas")
    if esta_completo(tablero, tablero_completo): # Valida si regresa porque está completo, entonces no se saca de la lista ni se pone en False el valor actual
      return

    solucion.pop() # Sacar ese ultimo elemento de la solucion
    tablero[coord_i][coord_j] = False # Marcarlo como aún no visitado
    return

  # print(f"Casillas: {casillas}")
  for c in casillas:
    backtracking_caballo(c[0], c[1])
    if esta_completo(tablero, tablero_completo): # Valida si regresa porque está completo, entonces no se saca de la lista ni se pone en False el valor actual
      return

  solucion.pop() # Sacar ese ultimo elemento de la solucion
  tablero[coord_i][coord_j] = False # Marcarlo como aún no visitado

backtracking_caballo(0, 0)

print("Solución")
print(solucion)

print("\nTablero completo")
for i in range(8):

  print(tablero[i])

import numpy as np
# Function to animate the knight's moves on a chessboard with marked visited squares
def animate_moves():
    fig, ax = plt.subplots()
    ax.set_xlim(-1, 8)
    ax.set_ylim(-1, 8)
    ax.set_aspect('equal')

    # Creating a chessboard grid
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                ax.add_patch(plt.Rectangle((i - 0.5, j - 0.5), 1, 1, color='white', linewidth=1, edgecolor='black'))
            else:
                ax.add_patch(plt.Rectangle((i - 0.5, j - 0.5), 1, 1, color='black', linewidth=1, edgecolor='black'))

    line, = ax.plot([], [], marker='o', color='red')

    visited_squares, = ax.plot([], [], marker='s', markersize=15, color='blue', linestyle='')

    def init():
        line.set_data([], [])
        visited_squares.set_data([], [])
        return line, visited_squares

    def animate(i):
        if i < len(solucion):
            x, y = solucion[i]
            print(f"Visitando ({[x]}, {[y]})")
            line.set_data([x], [y])
            visited_x = [pos[0] for pos in solucion[:i+1]]
            visited_y = [pos[1] for pos in solucion[:i+1]]
            visited_squares.set_data(visited_x, visited_y)
        return line, visited_squares

    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(solucion), interval=200, blit=True)
    plt.show()

# Create a simple Tkinter window
root = tk.Tk()
root.title("Knight's Moves Animation")

# Button to trigger animation
animate_button = tk.Button(root, text="Animate Knight's Moves", command=animate_moves)
animate_button.pack()

root.mainloop()