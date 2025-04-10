# This is a sample Python script.
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(m, n, matriz):
    matriz2= [[0]* n for _ in range(m)]
    matriz2[0][0]+=1
    for i, value in enumerate(matriz):
        for j, value2 in enumerate(value):
                if matriz[i][j] == 1:
                    matriz2[i][j] = 0
                else:
                    if i>0:
                        matriz2[i][j] += matriz2[i-1][j]
                    if j>0:
                        matriz2[i][j] += matriz2[i][j-1]

    return matriz2[m-1][n-1]
def funcion2():





if __name__ == '__main__':
    matriz_aleatoria = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
    print(print_hi(4,4, matriz_aleatoria))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
