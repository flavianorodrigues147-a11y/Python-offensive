numeros = [10, 20, 30, 40, 50]
soma = 0
for numero in numeros:
    soma += numero

media = soma / len(numeros)
print("A média é:", media)

# Explicação da solução
# Nesse código, temos uma lista de números chamada numeros. Para calcular a média, primeiro inicializamos uma variável soma com o valor zero. Em seguida, percorremos cada número na lista numeros usando um for loop for e adicionamos cada número à variável soma.

# Depois de percorrer todos os números, dividimos a soma pelo número total de elementos na lista numeros, que obtemos através da função len(). Com essa operação, obtemos a média. Então, ao final do código, exibimos a média usando a função print().

gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 400, 500, 700]

total_joao = sum(gastos_joao)
total_pedro = sum(gastos_pedro)
print("Total gasto por João:", total_joao)
print("Total gasto por Pedro:", total_pedro)

if total_joao > total_pedro:
    print("João gastou mais:", total_joao)

elif total_pedro > total_joao:
    print("Pedro gastou mais:", total_pedro)
else:
    print("Ambos gastaram a mesma quantia.")
