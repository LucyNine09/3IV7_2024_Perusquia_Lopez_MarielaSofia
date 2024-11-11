def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(str(elemento) for elemento in fila))

def transponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = [[matriz[j][i] for j in range(filas)] for i in range(columnas)]
    return transpuesta

tamaño = int(input("Ingrese el tamaño de la matriz (3 para 3x3 o 5 para 5x5): "))
if tamaño != 3 and tamaño != 5:
    print("Tamaño no válido. Solo se permite 3x3 o 5x5.")
    exit()

matriz = []
print(f"Ingrese los valores para una matriz de {tamaño}x{tamaño}:")
for i in range(tamaño):
    fila = []
    for j in range(tamaño):
        valor = int(input(f"Ingrese el valor para la posición ({i+1},{j+1}): "))
        fila.append(valor)
    matriz.append(fila)

print("\nMatriz original:")
imprimir_matriz(matriz)

matriz_transpuesta = transponer_matriz(matriz)
print("\nMatriz transpuesta:")
imprimir_matriz(matriz_transpuesta)
