# [PY-A02]
# Faça um programa que solicite ao usuário que digite 10 valores para
# preencher uma lista. Em seguida, o programa deve separar os números pares e 
# ímpares em listas diferentes. Por fim, exiba na tela os números pares, os 
# números ímpares em uma tupla, a quantidade de números pares e ímpares presentes 
# na lista, e a soma de todos os números pares e ímpares, respectivamente.

def ln(x):
    print("-"*x)

numeros = []
pares = []
impares = []

for i in range(10):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))

for i in numeros:
    if i%2==0:
        pares.append(i)
    elif i%2!=0:
        impares.append(i)

pares = tuple(pares)
impares = tuple(impares)

ln(20)
print("Números pares:")
ln(20)
print(f"    Quantidade de números pares: {len(pares)}")
print(f"    Soma de todos os números: {sum(pares)}")
print(f"    Todos os pares: {pares}\n\n")

ln(20)
print("Números impares:")
ln(20)
print(f"    Quantidade de números impares: {len(impares)}")
print(f"    Soma de todos os números: {sum(impares)}")
print(f"    Todos os impares: {impares}\n\n\n")
