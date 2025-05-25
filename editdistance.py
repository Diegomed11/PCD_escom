def edit_distance(str1, str2):
    # Longitudes de las cadenas
    len_str1 = len(str1)
    len_str2 = len(str2)
    # Crear una matriz para almacenar los resultados de subproblemas
    dp = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]
    # Inicializar la primera fila y la primera columna
    for i in range(len_str1 + 1):
        dp[i][0] = i  # Necesita i eliminaciones para convertir str1[0:i] a ""
    for j in range(len_str2 + 1):
        dp[0][j] = j  # Necesita j inserciones para convertir "" a str2[0:j]
    # Llenar la matriz dp
    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No se necesita ninguna operación
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,    # Eliminación
                    dp[i][j - 1] + 1,    # Inserción
                    dp[i - 1][j - 1] + 1  # Sustitución
                )
    return dp[len_str1][len_str2]
# Ejemplo de uso
str1 = "murcielago"
str2 = "archipielago"
print(f"La distancia de edición entre '{str1}' y '{str2}' es: {edit_distance(str1, str2)}")
