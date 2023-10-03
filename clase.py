matriz = 2
variable1 = 91283

def prueba():
    print("ss")
    print("hola")

prueba()

def rellenar_matriz(matriz, variable1, variable2):
    for i in range(matriz):
        for j in range(matriz):
            matriz[i][j] = variable1 + variable2
    return matriz
matriz = []
matriz = rellenar_matriz(matriz, 5, 2)

print(matriz)