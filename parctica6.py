import numpy as np
import matplotlib.pyplot as plt
intervalo=1
x=np.random.normal(1,2,100000)
min_value = np.floor(np.min(x))
max_value = np.ceil(np.max(x))
b = np.arange(min_value, max_value + intervalo, intervalo)
# Contar cuántos datos caen en cada intervalo
counts = np.zeros(len(b) - 1)
for value in x:
    for i in range(len(b) - 1):
        if b[i] <= value < b[i + 1]:
            counts[i] += 1
            break


# Graficar el histograma
plt.bar(b[:-1], counts, width=intervalo, align='edge', edgecolor='black')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')

plt.show()


