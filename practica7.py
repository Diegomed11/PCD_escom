'''
calcular los coeficientes a0 y a1 entre las combinaciones de variables de la base de datos iris.csv y graficar la regresion
calcular la suma frl valor absoluto R1
mencionar en la conclusion que combinacion de variables exhibe menor residuo y mas reciduo
dar interpretacion de los resultados
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el conjunto de datos
iris = pd.read_csv('C:/Users/legom/Documents/PCD\PCD_escom/iris.csv')

# Extraer las columnas necesarias
pw = iris["petal.width"]
pl = iris["petal.length"]
sw = iris["sepal.width"]
sl = iris["sepal.length"]

# Funciones para calcular a1 y a0
def a1(x, y):
    sx = np.sum(x)
    sy = np.sum(y)
    sxy = np.sum(x * y)
    sx2 = np.sum(x ** 2)
    return (len(x) * sxy - sy * sx) / (len(x) * sx2 - sx ** 2)

def a0(x, y):
    sx = np.sum(x)
    sy = np.sum(y)
    return (1 / len(x)) * (sy - a1(x, y) * sx)

# Función para calcular residuos y graficar
def calculate_and_plot(x, y, x_label, y_label):
    a1_value = a1(x, y)
    a0_value = a0(x, y)

    # Predicciones
    y_pred = a0_value + a1_value * x
    residuos = y - y_pred
    suma_residuos_absolutos = np.sum(np.abs(residuos))

    # Graficar
    plt.scatter(x, y, color='blue', label='Datos Observados')
    plt.plot(x, y_pred, color='red', label='Regresión Lineal')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(f'Regresión Lineal entre {x_label} y {y_label}')
    plt.legend()
    plt.show()

    return suma_residuos_absolutos, a0_value, a1_value

# Combinaciones de variables
combinaciones = [
    (pw, pl, "Petal Width", "Petal Length"),
    (pw, sw, "Petal Width", "Sepal Width"),
    (pw, sl, "Petal Width", "Sepal Length"),
    (pl, sw, "Petal Length", "Sepal Width"),
    (pl, sl, "Petal Length", "Sepal Length"),
    (sw, sl, "Sepal Width", "Sepal Length")
]

resultados = []

# Calcular y graficar para cada combinación
for x, y, x_label, y_label in combinaciones:
    suma_residuos, a0_value, a1_value = calculate_and_plot(x, y, x_label, y_label)
    resultados.append((x_label, y_label, a0_value, a1_value, suma_residuos))

# Mostrar resultados
for res in resultados:
    print(f"Combinación: {res[0]} vs {res[1]} | a0: {res[2]:.4f}, a1: {res[3]:.4f}, Suma de Residuos Absolutos: {res[4]:.4f}")

# Análisis de resultados
min_residuos = min(resultados, key=lambda x: x[4])
max_residuos = max(resultados, key=lambda x: x[4])

print("\nConclusiones:")
print(f"La combinación de variables con menor residuo es: {min_residuos[0]} vs {min_residuos[1]} con una suma de residuos absolutos de {min_residuos[4]:.4f}.")
print(f"La combinación de variables con mayor residuo es: {max_residuos[0]} vs {max_residuos[1]} con una suma de residuos absolutos de {max_residuos[4]:.4f}.")

