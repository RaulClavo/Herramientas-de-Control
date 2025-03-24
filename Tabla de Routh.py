import sympy as sp

def tabla_routh(coefficients):
    fila1, fila2 = coefficients[::2], coefficients[1::2]
    max_len = max(len(fila1), len(fila2))
    fila1.extend([0] * (max_len - len(fila1)))
    fila2.extend([0] * (max_len - len(fila2)))
    tabla = [fila1, fila2]

    for i in range(2, len(coefficients)):
        nueva_fila = [((-tabla[-2][0] * tabla[-1][j + 1]) + (tabla[-2][j + 1] * tabla[-1][0])) / tabla[-1][0] for j in range(len(tabla[-1]) - 1)]
        nueva_fila.extend([0] * (max_len - len(nueva_fila)))
        tabla.append(nueva_fila)
        if all(v == 0 for v in nueva_fila): break

    print("")
    for fila in tabla: print([i for i in fila if i != 0])
      
def convertir_entrada(entrada):
    return [int(e.strip()) if e.strip().isdigit() else sp.symbols(e.strip()) for e in entrada.split(',')]

tabla_routh(convertir_entrada(input("Introduce los coeficientes separados por comas (números o variables): ")))
