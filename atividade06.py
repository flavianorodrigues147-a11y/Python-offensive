def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


# Chamada da função e impressão do resultado para o número 5
print(fatorial(5))
